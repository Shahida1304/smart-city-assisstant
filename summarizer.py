import streamlit as st
from PyPDF2 import PdfReader
import docx
from ibm_watsonx_ai.foundation_models.model import Model


# Function to summarize text using IBM Granite
def summarize_text(text):
    if len(text) > 5000:
        text = text[:5000]

    try:
        # ✅ Use secrets securely
        model = Model(
            model_id=st.secrets["MODEL_ID"],
            credentials={
                "apikey": st.secrets["IBM_GRANITE_API_KEY"],
                "url": st.secrets["IBM_GRANITE_URL"],
            },
            project_id=st.secrets["IBM_GRANITE_PROJECT_ID"],
        )

        prompt = f"Summarize this text clearly:\n\n{text}"

        response = model.generate_text(
            prompt=prompt,
            params={
                "max_new_tokens": 300,
                "temperature": 0.5,
                "top_p": 0.9,
                "decoding_method": "sample",
                "stop_sequences": [],
            },
        )

        # The SDK usually returns just a string
        return response if isinstance(response, str) else str(response)

    except Exception as e:
        st.error(f"IBM SDK Error: {str(e)}")
        return None


# File text extraction
def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.type

    if "text/plain" in file_type:
        return uploaded_file.read().decode("utf-8")
    elif "application/pdf" in file_type:
        reader = PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    elif (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        in file_type
    ):
        doc = docx.Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    return None


# Streamlit app UI
def run_summarizer():
    st.set_page_config(page_title="IBM Granite Summarizer", page_icon="📝")
    st.title("📝 Text & Document Summarizer using IBM Granite")

    option = st.radio("Choose input type:", ["Text", "Document"])
    text = ""

    if option == "Text":
        text = st.text_area("Enter text to summarize", height=200)
    else:
        uploaded_file = st.file_uploader(
            "Upload document (TXT, PDF, DOCX)", type=["txt", "pdf", "docx"]
        )
        if uploaded_file:
            text = extract_text_from_file(uploaded_file)
            st.text_area("Extracted Text Preview", value=text, height=200)

    if text and st.button("Summarize"):
        with st.spinner("Generating summary..."):
            summary = summarize_text(text)
            if summary:
                st.success("✅ Summary:")
                st.write(summary)

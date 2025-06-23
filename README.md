Smart City Assistant


Smart City Assistant is a multi-functional dashboard built using Streamlit, designed to promote smart governance, sustainability, and public utility engagement. It integrates weather forecasts, pollution tracking, traffic monitoring, document summarization, chatbot interactions, KPI forecasting, customer feedback collection, anomaly detection, and eco-awareness tips.

Features

1. Weather Forecast
   
View current temperature, humidity, pressure, and wind speed.

7-day weather forecast with charts and statistics.

Powered by OpenWeatherMap API.

2. Air Pollution Monitoring
   
Fetch and display AQI (Air Quality Index) for Indian cities.

Uses geographical coordinates to pull real-time AQI.

3. Traffic Monitoring
   
Displays real-time traffic data using TomTom API.

Visualizes congestion status per location.

4. Policy Summarizer
   
Summarizes text or uploaded documents (TXT, PDF, DOCX).

Uses IBM Watsonx Granite LLM API for advanced summarization.

5. Chat Assistant
   
Smart chatbot trained for sustainable city Q&A.

Uses IBM Granite instruct model for real-time replies.


6. KPI Forecasting
   
Upload previous KPI data in CSV format.

Uses Prophet model to predict future values for up to 5 years.

7. Customer Feedback Form
   
Collects user input, suggestions, or complaints.

Stores feedback locally in a structured format.

8. Anomaly Detection
    
Detect unusual data patterns in uploaded sensor or metric data.

Uses Isolation Forest for unsupervised outlier detection.

9. Eco Tips
    
Random daily tips on water, energy, waste, and transport.

Users can submit their own tips.

Setup Instructions

1. Clone the repository
   
git clone https://github.com/yourusername/smart-city-assistant.git

cd smart-city-assistant

2. Create .env file
   
touch .env

Add your API keys:

openweathermap_api=YOUR_OPENWEATHERMAP_KEY

TOMTOM_API_KEY=YOUR_TOMTOM_KEY

IBM_GRANITE_API_KEY=YOUR_IBM_KEY

IBM_GRANITE_PROJECT_ID=YOUR_IBM_PROJECT_ID

IBM_GRANITE_URL=https://us-south.ml.cloud.ibm.com

MODEL_ID=granite-3b-instruct

3. Install dependencies
   
pip install -r requirements.txt

4. Run the application
   
streamlit run app.py

Requirements

All dependencies are listed in requirements.txt. Major packages include:

streamlit

python-dotenv

requests

pandas, numpy

matplotlib, seaborn

scikit-learn

prophet

ibm-watsonx-ai

PyPDF2, python-docx


Sample Files

dummy_kpi.csv – for KPI forecasting

dummy_anomaly_data.csv – for anomaly detection

Contribution

Contributions are welcome. Feel free to raise an issue or submit a pull request for improvements, additional modules, or bug fixes.


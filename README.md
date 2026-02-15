# Volt_Veda AI ⚡🔋  
Battery Health Predictor using Machine Learning + FastAPI + Streamlit

VoltVeda AI is a complete end-to-end Machine Learning project that predicts the battery health percentage of a smartphone based on usage habits, charging behavior, and thermal stress factors.

This project contains:
- A FastAPI backend (ML Prediction API)
- A Streamlit frontend (User Interface)
- A trained ML pipeline model (.pkl)
- Deployment-ready structure (Railway supported)

------------------------------------------------------------

## 🚀 Live Deployment
live_link: https://talented-happiness-production-89a5.up.railway.app/

Frontend (Streamlit App):
https://talented-happiness-production-89a5.up.railway.app

Backend (FastAPI API):
https://voltveda-production.up.railway.app

FastAPI Docs (Swagger UI):
https://voltveda-production.up.railway.app/docs

------------------------------------------------------------

## 📌 Features

✔ Predict Battery Health Percentage  
✔ Shows Health Status (GOOD / MODERATE / BAD)  
✔ Gives battery safety suggestions  
✔ Fully working frontend + backend integration  
✔ Deployable on Railway / Render / Cloud platforms  
✔ Model loaded using Joblib (.pkl pipeline)

------------------------------------------------------------

## 🏗 Project Structure

Volt_Veda/
│
├── app/
│   ├── main.py
│   └── model/
│       └── Battery_health_pipeline.pkl
│
├── dataset/
│   ├── battery_dataset_update.csv
│   └── smartphone_battery_features.csv
│
├── frontend/
│   ├── frontend.py
│   └── requirements.txt
│
├── notebook/
│   └── train.ipynb
│
├── requirements.txt
├── runtime.txt
├── .gitignore
└── README.md

------------------------------------------------------------

## ⚙ Tech Stack

Backend:
- FastAPI
- Uvicorn
- Pydantic
- Python-Multipart
- CORSMiddleware

Frontend:
- Streamlit
- Requests

Machine Learning:
- Scikit-learn
- Pandas
- NumPy
- Joblib

Deployment:
- Railway

------------------------------------------------------------

## 🧠 Machine Learning Model Details

Algorithm Used:
- Linear Regression Pipeline

Pipeline Includes:
- Data preprocessing
- Feature scaling (if applied)
- Model training
- Full pipeline saved as .pkl

Model File Location:
app/model/Battery_health_pipeline.pkl

------------------------------------------------------------

## 🔥 API Endpoint Details (FastAPI)

Base URL:
https://voltveda-production.up.railway.app

Endpoint:
POST /predict

------------------------------------------------------------

## 📩 Request Body Example

{
  "device_age_months": 18,
  "battery_capacity_mah": 5000,
  "avg_screen_on_hours_per_day": 6.5,
  "avg_charging_cycles_per_week": 7,
  "avg_battery_temp_celsius": 34,
  "fast_charging_usage_percent": 60,
  "overnight_charging_freq_per_week": 4,
  "gaming_hours_per_week": 5,
  "video_streaming_hours_per_week": 10,
  "charging_habit_score": 8,
  "usage_intensity_score": 9.5,
  "thermal_stress_index": 6.2
}

------------------------------------------------------------

## 📤 Response Example

{
  "predicted_battery_health_percent": 83.45,
  "health_status": "GOOD",
  "message": "Battery health is good. Avoid overheating and reduce fast charging."
}

------------------------------------------------------------

## 🖥 Running Backend Locally

Step 1: Go to project folder
cd Volt_Veda

Step 2: Create virtual environment
python -m venv myenv

Step 3: Activate virtual environment
myenv\Scripts\activate

Step 4: Install requirements
pip install -r requirements.txt

Step 5: Run FastAPI backend
uvicorn app.main:app --reload

Backend will run on:
http://127.0.0.1:8000

Swagger Docs:
http://127.0.0.1:8000/docs

------------------------------------------------------------

## 🎨 Running Frontend Locally (Streamlit)

Step 1: Go to frontend folder
cd frontend

Step 2: Install frontend requirements
pip install -r requirements.txt

Step 3: Run Streamlit app
streamlit run frontend.py

Frontend will run on:
http://localhost:8501

------------------------------------------------------------

## 🌍 Deployment Notes (Railway)

Backend Deployment Start Command:
uvicorn app.main:app --host 0.0.0.0 --port $PORT

Frontend Deployment Start Command:
cd frontend && streamlit run frontend.py --server.port $PORT --server.address 0.0.0.0

Frontend Build Command:
cd frontend && pip install -r requirements.txt

------------------------------------------------------------

## 🔒 CORS Fix (Important)

CORS middleware is added in FastAPI backend to allow frontend requests:

allow_origins=["*"]
allow_methods=["*"]
allow_headers=["*"]

------------------------------------------------------------

## 📌 Future Improvements

- Add authentication (JWT)
- Improve ML model accuracy using RandomForest/XGBoost
- Add database support for storing predictions
- Add visualization graphs in Streamlit dashboard
- Add CI/CD pipeline

------------------------------------------------------------

## 👨‍💻 Author

Developed by: Biman Adhikary  
Project Name: VoltVeda AI  
GitHub: https://github.com/biman2006/Volt_Veda

------------------------------------------------------------

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub!

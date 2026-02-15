# ⚡ Volt_Veda — Smartphone Battery Health Predictor (ML + FastAPI + Streamlit)

VoltVeda is a real-world Machine Learning project that predicts a smartphone’s **Battery Health Percentage** based on usage behavior, thermal stress, charging habits, and device age.

This project is deployed with:
- **FastAPI** as the backend inference API
- **Streamlit** as the frontend UI
- **Scikit-learn Pipeline + ColumnTransformer** for robust preprocessing and prediction

---

## 🚀 Live Demo

### 🌐 Frontend (Streamlit UI)
🔗 https://talented-happiness-production-89a5.up.railway.app

### ⚙️ Backend (FastAPI API)
🔗 https://voltveda-production.up.railway.app

### 📌 API Documentation (Swagger UI)
🔗 https://voltveda-production.up.railway.app/docs

---

## 📌 Project Features

✅ Predicts **Battery Health Percentage** using Linear Regression  
✅ Uses **PowerTransformer (Yeo-Johnson)** to reduce skewness  
✅ Handles missing values using **SimpleImputer**  
✅ Scales numerical features using **StandardScaler**  
✅ Encodes categorical features using **OneHotEncoder**  
✅ Fully production-ready ML pipeline saved using `joblib`  
✅ FastAPI endpoint for real-time predictions  
✅ Streamlit frontend for user-friendly interaction  
✅ Deployed on Railway with public domains

---

## 🧠 Machine Learning Model

- **Algorithm**: Linear Regression
- **Evaluation Metric**: R² Score
- **Achieved Performance**: ~0.95 R² Score (excellent prediction accuracy)

---

## 🏗️ Tech Stack

### Backend
- FastAPI
- Pydantic
- Uvicorn

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Frontend
- Streamlit
- Requests

### Deployment
- Railway Cloud

---

## 📂 Project Structure

Volt_Veda/
│
├── app/
│ ├── main.py # FastAPI backend API
│ ├── model/
│ │ └── Battery_health_pipeline.pkl # Trained ML pipeline
│
├── frontend/
│ ├── frontend.py # Streamlit UI
│ └── requirements.txt # Streamlit dependencies
│
├── notebook/
│ └── model_training.ipynb # Model training notebook (optional)
│
├── requirements.txt # Backend requirements
├── runtime.txt # Python runtime version (optional)
├── README.md # Project documentation
└── .gitignore


---


---

## 🔥 API Endpoints

### ✅ Health Check
`GET /`

Returns a basic message confirming API is running.

Example response:
```json
{
  "message": "Battery Health Predictor API Running 🚀"
}
✅ Battery Health Prediction
POST /predict

Request Body Example:
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
Response Example:
{
  "predicted_battery_health_percent": 83.45,
  "health_status": "GOOD",
  "message": "Battery health is good. Avoid overheating and reduce fast charging."
}
⚙️ Installation & Setup (Local)
1️⃣ Clone Repository
git clone https://github.com/biman2006/Volt_Veda.git
cd Volt_Veda
2️⃣ Create Virtual Environment
python -m venv myenv
Activate:

Windows (PowerShell)
myenv\Scripts\activate
Mac/Linux
source myenv/bin/activate
3️⃣ Install Backend Dependencies
pip install -r requirements.txt
4️⃣ Run FastAPI Backend
uvicorn app.main:app --reload
Backend will run on:
📌 http://127.0.0.1:8000

Swagger Docs:
📌 http://127.0.0.1:8000/docs

🎨 Running Streamlit Frontend (Local)
1️⃣ Install Streamlit Dependencies
pip install -r frontend/requirements.txt
2️⃣ Run Streamlit App
streamlit run frontend/frontend.py
Frontend will run on:
📌 http://localhost:8501

🌍 Deployment Notes
This project is deployed on Railway with two services:

✅ Backend Deployment (FastAPI)
Start Command:

uvicorn app.main:app --host 0.0.0.0 --port $PORT
✅ Frontend Deployment (Streamlit)
Start Command:

streamlit run frontend/frontend.py --server.port $PORT --server.address 0.0.0.0
🔐 CORS Support
To allow frontend-backend communication, CORS middleware is enabled in FastAPI:

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
📌 Future Improvements
🚀 Possible upgrades for VoltVeda:

Add user authentication (JWT)

Store prediction history using PostgreSQL

Improve model using RandomForest / XGBoost

Add feature importance visualization

Add battery replacement recommendations based on threshold

👨‍💻 Author
Biman Adhikary
📌 GitHub: https://github.com/biman2006

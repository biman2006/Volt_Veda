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

## 🔥 API ENDPOINTS 

### ✅ Health Check

`GET /`

Returns a basic message confirming API is running.

Example response:
```json
{
  "message": "Battery Health Predictor API Running 🚀"
}

---

##✅ Battery Health Prediction



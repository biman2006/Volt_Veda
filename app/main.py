from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Annotated, Literal
import os

import joblib 
import pandas as pd 





app=FastAPI(
    title="Battery Health Predictor API",
    description=""" 

🚀**Battery Health predictor Api**

This APP predicts the **battery health percentage** of a smartphone based on usage, charging habits, and thermal stress factors.

📌** Machine Learning Model: ** Linear Regression (pipeline + Columntransformer)
📌** Input:** Device usage & charging behavior
📌 **Output** predicted battery health percentage 
""",

version="1.0.0",
contact={
    "name": "Biman Adhikary",
    "Email":"bimanadhikary75@gmail.com",
    "url": "https://github.com/biman2006"
},
license_info={
    "name": "MIT License",
    "url": "https://opensource.org/licenses/MIT"
}

)




import os
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model", "Battery_health_pipeline.pkl")
model = joblib.load(model_path)



class BatteryInput(BaseModel):
    device_age_months: Annotated[float, Field(..., description="Age of the Mobile in months", example=18)]
    battery_capacity_mah: Annotated[float, Field(..., description="Battery Capacity In mAh", example=5000)]
    avg_screen_on_hours_per_day: Annotated[float, Field(..., description="avg screen time per day in hours", example=6.5)]
    avg_charging_cycles_per_week: Annotated[float, Field(..., description="Charging cycle per week in hour", example=10)]
    avg_battery_temp_celsius: Annotated[float, Field(..., description="Average battery temperature in celcius", example=34)]
    fast_charging_usage_percent: Annotated[float, Field(..., description="Fast Charging usage percentage(0-100)%", example=60)]
    overnight_charging_freq_per_week: Annotated[float, Field(..., description="Overnight charging frequency per week", example=4)]
    gaming_hours_per_week: Annotated[float, Field(..., description="Gaming hours per week", example=12)]
    video_streaming_hours_per_week: Annotated[float, Field(..., description="Streaming hours per week", example=8)]

    charging_habit_score: Annotated[float, Field(..., description="Charging habit score (0-10)", example=7.5)]
    usage_intensity_score: Annotated[float, Field(..., description="Usage intensity score (0-10)", example=8.2)]
    thermal_stress_index: Annotated[float, Field(..., description="Thermal stress index (0-10)", example=6.8)]

    background_app_usage_level:Annotated[Literal['Medium', 'High', 'Low'], Field(...,description="Enter background app usage level(Medium, High, Low)", example="Medium")]
    signal_strength_avg: Annotated[
    Literal['Medium', 'High', 'Low'],
    Field(
        ...,
        description="Enter signal strength average ('Medium', 'High', 'Low')",
        example="High"
    )
]



class BatteryPredictonResponse(BaseModel):
    predicted_battery_health_percent:float=Field(...,example=82.45, description="Predicted battery Health Percentage")
    health_status:str=Field(...,example="GOOD", description="Battery health category")
    message:str=Field(...,example="Battery health is good . keep avoiding overheating.")


@app.get("/", tags=["Home"])
def home():
        """
        Root endpoint to verify API is running
        """

        return{
            "status": "Success",
            "message":"Battery Health Predictor API Running 🚀 ",
            "Developer": "Biman Adhikary",
            "Model_Type":"Linear Regression Pipeline",
            "version":"1.0.0"
        }
    

@app.post("/predict", response_model=BatteryPredictonResponse, tags=["prediction"])
def predict_battery_health(data:BatteryInput):
     """ 
     Predict battery health percentage based on user input features.


     Steps:
     -Convert input JSON into pandas Dataframe
     -Pass it into the trained ML pipeline
     -Return predicted battery health percentage + Status message 
     """
     try:
          input_df=pd.DataFrame([data.model_dump()])

          prediction=model.predict(input_df)[0]
          prediction=round(float(prediction),2)



          if prediction>=85:
               status="Excellent ✅"
               msg="Battery health is excellent. Keep maintaining good charging habits."
          elif prediction>=70:
               status="GOOD 🟢"
               msg="Battery health is good. Avoid overheating and reduce fast charging."
          else:
               status="POOR 🔴"
               msg="Battery health is poor. Battery replacement may be needed soon."


          return{
               "predicted_battery_health_percent": prediction,
               "health_status": status,
               "message":msg
          }

     except Exception as e:
          raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")




# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# 모델 로드
model = joblib.load("model.pkl")
app = FastAPI()


# 입력 스키마 정의
class InputData(BaseModel):
    features: list[float]


@app.get("/")
def read_root():
    return {"message": "AI Model Server"}


@app.post("/predict")
def predict(data: InputData):
    input_array = np.array(data.features).reshape(1, -1)
    prediction = model.predict(input_array)
    return {"prediction": prediction.tolist()}

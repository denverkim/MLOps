# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")


# 요청 데이터 스키마
class InputData(BaseModel):
    x: float


@app.get("/")
def root():
    return {"message": "FastAPI 예측 서버에 오신 것을 환영합니다!"}


@app.post("/predict/")
def predict(data: InputData):
    X = np.array([[data.x]])
    y_pred = model.predict(X)
    return {"input": data.x, "prediction": y_pred[0]}

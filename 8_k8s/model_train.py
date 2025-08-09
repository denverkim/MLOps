# model_train.py
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib
import os

# 3개의 특성(features)을 갖는 입력 데이터 (입력: 2D, 출력: 1D)
X = np.array([[1.0, 2.0, 3.0], [2.0, 3.0, 4.0], [3.0, 4.0, 5.0], [4.0, 5.0, 6.0]])

# 출력값 (예: y = x1 + x2 + x3)
y = np.array([6.0, 9.0, 12.0, 15.0])

# 모델 정의 및 학습
model = LinearRegression()
model.fit(X, y)

# 모델 저장 디렉토리 생성 및 저장
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")

print("선형 회귀 모델이 model/model.pkl에 저장되었습니다.")

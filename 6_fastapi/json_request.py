import requests

# 서버 주소
url = "http://127.0.0.1:8000/predict/"

# 예측할 입력 데이터 (JSON 형태로)
input_data = {"x": 5.0}

# POST 요청 보내기
response = requests.post(url, json=input_data)

# 결과 출력
print("Status code:", response.status_code)
print("응답 JSON:", response.json())


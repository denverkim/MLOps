# 베이스 이미지
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 모델과 앱 복사
COPY model.pkl /app/model.pkl
COPY app /app

# 필요한 라이브러리 설치
RUN pip install --no-cache-dir -r requirements.txt

# API 서버 실행 명령
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

ARG APP_FILE=app_v1.py
FROM python:3.12-slim
		
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
		
COPY ${APP_FILE} app.py
		
EXPOSE 5000
CMD ["python", "app.py"]

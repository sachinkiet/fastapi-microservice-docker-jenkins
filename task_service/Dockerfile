FROM python:3.11-slim

WORKDIR /task_service
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["uvicorn", "task_app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload", "--reload-dir", "/task_service"]

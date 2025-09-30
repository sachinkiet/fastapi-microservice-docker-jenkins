FROM python:3.11-slim

# Set work directory
WORKDIR /user_service

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Run FastAPI app
CMD ["uvicorn", "user_app.main:app", "--host", "0.0.0.0", "--port", "8002", "--reload", "--reload-dir", "/user_service"]

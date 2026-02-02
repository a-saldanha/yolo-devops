FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Install dependencies (CPU-only torch + headless opencv)
RUN pip install --no-cache-dir -r requirements.txt

# --- NOTE: The apt-get line is GONE ---

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
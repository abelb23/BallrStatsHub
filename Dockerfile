# Python Version 3.14.7
FROM python:3.14.7

# Work Directory is /backend
WORKDIR /backend

# Copy backend to container
COPY backend .

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the container to port 8000
EXPOSE 8000

WORKDIR /backend/app

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


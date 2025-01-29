# Use official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy project files
COPY requirements.txt ./
COPY app/ ./app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for FastAPI
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

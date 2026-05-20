# Use a lightweight, official python slim base image
FROM python:3.12-slim

# Set environment system configurations
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for compiling postgres libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies first to leverage Docker build cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend codebase
COPY . /app/

# Expose Django REST API service port
EXPOSE 8000

# Default entrypoint command (easily overridden in docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

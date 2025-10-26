# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies including Node.js
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    ffmpeg \
    && curl -sL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Copy backend files
COPY backend/ ./backend

# Copy frontend files
COPY frontend/ ./frontend

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Build frontend
WORKDIR /app/frontend
RUN npm install && npm run build

# Switch back to app directory
WORKDIR /app

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "backend/main.py"]
# Use Python 3.9 slim as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file first (to leverage Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the required files explicitly
COPY app.py .
COPY model.py .
COPY salary_data.csv .
COPY templates/ ./templates/

# Optional: Copy tests if needed for debugging
# COPY test_app.py .
# COPY test_model.py .

# Run model training to generate model.pkl
RUN python model.py

# Expose the port your Flask app runs on
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]

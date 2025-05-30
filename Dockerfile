FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your code including model.py and app.py
COPY . .

# Run model.py to create model.pkl inside the container
RUN python model.py

# Expose port your app listens on
EXPOSE 5000

# Run your app
CMD ["python", "app.py"]

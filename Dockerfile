FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files from current directory to /app inside the container
COPY . .

# Debug: List all files to confirm salary_data.csv exists
RUN echo "🔍 Files in /app after COPY:" && ls -al /app

# Debug: Check if salary_data.csv is present
RUN if [ -f "salary_data.csv" ]; then echo "✅ salary_data.csv found"; else echo "❌ salary_data.csv MISSING"; fi

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the model script (should now find the CSV)
RUN python model.py

# Expose port
EXPOSE 5000

# Start app
CMD ["python", "app.py"]

FROM python:3.9-slim

WORKDIR /app

# Copy everything from local folder to /app in the image
COPY . .

# List all files copied inside /app to debug
RUN echo "🔍 Files in /app after COPY:" && ls -al /app

# (Optional) List templates dir to check
RUN echo "📂 Files in /app/templates:" && ls -al /app/templates

# Continue with your build steps ...
RUN pip install --no-cache-dir -r requirements.txt
RUN python model.py

EXPOSE 5000
CMD ["python", "app.py"]

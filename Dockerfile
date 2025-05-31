FROM python:3.9-slim

WORKDIR /app

# Debug: List files in the context before COPY to troubleshoot missing files
# This line will not work directly in Dockerfile, but we use RUN ls after COPY to inspect
# So instead, first copy everything to inspect
COPY . .

# List files to debug what's present inside the image after copying
RUN echo "🔍 Contents of /app after COPY:" && ls -al /app && echo "📂 /app/templates:" && ls -al /app/templates

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run model.py to generate model.pkl
RUN python model.py

# Expose app port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]

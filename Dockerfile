FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Verify files are present
RUN ls -la && \
    echo "Checking for salary_data.csv..." && \
    if [ -f "salary_data.csv" ]; then echo "File found"; else echo "File missing"; exit 1; fi

RUN python model.py

EXPOSE 5000
CMD ["python", "app.py"]
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir flask psycopg2-binary

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]


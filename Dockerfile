FROM python:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app/ .
EXPOSE 8080
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "--certfile=/certs/tls.crt", "--keyfile=/certs/tls.key", "app.controller:app"]

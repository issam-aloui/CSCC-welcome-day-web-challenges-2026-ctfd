FROM python:3.11-slim-bookworm
WORKDIR /app
RUN pip install --no-cache-dir flask
COPY . /app
ENTRYPOINT ["python", "app.py"]

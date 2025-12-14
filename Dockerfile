FROM python:3.11-slim

WORKDIR /app

COPY index.py .


RUN pip install --no-cache-dir flask

CMD ["python", "index.py"]
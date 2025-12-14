FROM python:3.11-slim

WORKDIR /app

COPY index.py .

CMD ["python", "index.py"]
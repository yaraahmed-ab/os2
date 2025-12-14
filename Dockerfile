FROM python:3.11-slim

WORKDIR /app

COPY index.py .

RUN pip install 

CMD ["python", "index.py"]
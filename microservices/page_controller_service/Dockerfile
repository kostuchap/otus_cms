FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["uvicorn", "microservices.page_controller_service.app:app", "--host", "0.0.0.0", "--port", "5005"]
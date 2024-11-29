FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app


# nohup python main.py
# CMD ["python", "app.py"]
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5001"]
CMD ["uvicorn", "microservices.component_service.app:app", "--host", "0.0.0.0", "--port", "5001"]
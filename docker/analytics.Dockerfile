FROM python:3.10-slim

WORKDIR /app

COPY analytics-service/requirements.txt .
RUN pip install -r requirements.txt

COPY analytics-service/ .
COPY common/ /app/common/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
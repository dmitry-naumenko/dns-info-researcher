FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements .
RUN pip install -r production.txt

COPY ./app /app
EXPOSE 8002
CMD ["uvicorn", "app.main:app", "--host", "localhost", "--port", "8002"]

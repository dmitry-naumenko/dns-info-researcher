FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements .
RUN pip install -r production.txt
ARG APP_HOME=/app
WORKDIR ${APP_HOME}

FROM python:3.7-alpine
MAINTAINER Amir Anwar

# Recommended setting for running python in docker containers
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Add a new user and switch to it, if we don't do that, the root user will be the one running the application
RUN adduser -D user
USER user

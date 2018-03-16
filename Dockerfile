FROM python:3.7-rc-alpine

WORKDIR /app

APP . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

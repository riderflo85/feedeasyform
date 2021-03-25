FROM python:3.8

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y postgresql-server-dev-11 gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile .
RUN pipenv install

COPY . .

RUN mkdir ./feedeasyform_project/media
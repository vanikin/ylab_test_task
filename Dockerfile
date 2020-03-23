FROM python:3

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY . /code/
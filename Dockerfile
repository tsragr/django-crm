FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /usr/src/crm

COPY ./requirements.txt /usr/src/crm/requirements.txt
RUN pip install -r /usr/src/crm/requirements.txt

COPY . .



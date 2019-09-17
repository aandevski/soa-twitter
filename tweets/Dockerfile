FROM python:3.7-stretch

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app


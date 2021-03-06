FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip build-essential
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV FLASK_APP=./pdv_challenge/http/index.py

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

#CMD ["python3", "-m", "flask", "run", "-h", "0.0.0.0"]


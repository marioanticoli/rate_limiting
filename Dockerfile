FROM python:latest
ADD . /usr/app
WORKDIR /usr/app
RUN pip3 install -r requirements.txt

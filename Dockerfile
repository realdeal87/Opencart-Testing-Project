FROM python:3.7.4-stretch

RUN apt-get update && apt-get upgrade -y && apt-get -y install firefox-esr chromium git

WORKDIR /usr/src/test-framework

COPY . .

RUN git pull origin

ENV PATH /usr/src/test-framework:$PATH

RUN pip3 install -U pip

RUN pip3 install -r requirements.txt

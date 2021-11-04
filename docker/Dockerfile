#ベースイメージは、Ubuntu(Linux OS)をインストール
FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN pip3 install flask
RUN pip install opencv – python

# Docker内で
WORKDIR /home
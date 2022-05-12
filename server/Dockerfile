FROM python:3.8



ADD . /capstone/server

WORKDIR /capstone/server

RUN apt-get update

RUN pip install flask
RUN pip install pymysql



CMD python run.py
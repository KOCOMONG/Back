FROM python:3.8

ADD . /server

RUN apt-get update

RUN pip install flask

RUN cd server

CMD python run.py
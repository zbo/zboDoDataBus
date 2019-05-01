# base image
FROM python:3.6.8-slim

# MAINTAINER
MAINTAINER zbo2@qq.com

RUN pip install pyecharts
RUN mkdir /bob

WORKDIR /bob
COPY ./start.sh ./
COPY ./page.py ./

RUN chmod 777 ./start.sh

CMD [ "sh", "./start.sh" ]
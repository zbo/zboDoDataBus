# base image
FROM python:3.6.8-slim

# MAINTAINER
MAINTAINER zbo2@qq.com

RUN pip install jupyter
RUN mkdir /bob

COPY ./start.sh ./

RUN chmod 777 ./start.sh

CMD [ "sh", "./start.sh" ]
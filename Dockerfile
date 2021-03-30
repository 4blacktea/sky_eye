FROM centos:8.2.2004

RUN mkdir /app
COPY ./ /app
WORKDIR /app
RUN yum install python38 -y
RUN pip3 install -r /app/src/requirements.txt
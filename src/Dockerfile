FROM centos:centos7

RUN mkdir /app
COPY ./ /app
WORKDIR /app
RUN yum install python3 -y
RUN yum install gcc -y
RUN yum install -y python3-pip python3 python3-setuptools
RUN yum install -y python3-devel.x86_64
RUN yum install -y tar.x86_64
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt
RUN chmod +x run.sh
RUN yum install nmap -y
RUN curl https://intoli.com/install-google-chrome.sh | bash
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

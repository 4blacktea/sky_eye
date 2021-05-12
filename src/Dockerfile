FROM centos:7.8.2003

RUN mkdir /app
COPY ./ /app
WORKDIR /app
RUN yum install python38 -y
RUN pip3 install -r requirements.txt
RUN chmod +x run.sh
RUN yum install nmap -y
RUN curl https://intoli.com/install-google-chrome.sh | bash
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

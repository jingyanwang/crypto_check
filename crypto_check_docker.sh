docker build -t yanliang12/crypto_check:1.0.1 .

docker login --username yanliang12
Ng34ui378df

docker push yanliang12/crypto_check:1.0.1

docker run -it ^
-v "C:\Users\jimwa\Documents\proj_freelancer_220412\crypto_check":/crypto_check/ ^
yanliang12/crypto_check:1.0.1 

python3 crypto_check_flask_run.py


############Dockerfile###########
FROM openjdk:8

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y git 
RUN apt-get install -y curl
RUN apt-get install -y vim
RUN apt-get install -y tar
RUN apt-get install -y bzip2

RUN apt-get update
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip

####neo4j
RUN pip3 install gdown==3.12.2
RUN pip3 install rdflib==5.0.0
RUN pip3 install requests==2.24.0
RUN pip3 install pandas==1.1.3
RUN pip3 install elasticsearch==7.11.0
RUN pip3 install pyspark==3.1.1
RUN pip3 install esdk-obs-python==3.20.11 --trusted-host pypi.org
RUN pip3 install Pillow==8.2.0
RUN pip3 install xlrd==1.2.0
RUN pip3 install xlsxwriter==1.2.8
RUN pip3 install pprintpp==0.4.0

RUN pip3 install Flask==2.1.1
RUN pip3 install pprint36==3.9.0.2


WORKDIR /

####

RUN mkdir /home/yan
RUN chmod 777 /home/yan

RUN useradd -u 8877 yan
USER yan

####

ENV PYSPARK_PYTHON=/usr/bin/python3
ENV PYSPARK_DRIVER_PYTHON=/usr/bin/python3

####

WORKDIR /home/yan/

RUN echo "d4s5g1s2g1s2g1s5"

RUN git clone https://github.com/yanliang12/yan_webpage_download.git
RUN mv yan_webpage_download/* ./
RUN rm -r yan_webpage_download


RUN git clone https://github.com/jingyanwang/crypto_check.git
RUN mv crypto_check/* ./
RUN rm -r crypto_check

############Dockerfile############
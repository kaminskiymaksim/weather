FROM ubuntu:latest
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install pyowm
COPY weather.py /home/weather.py 
ENTRYPOINT ["/usr/bin/python3", "./weather.py"]  

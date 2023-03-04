FROM python:3.8-slim


WORKDIR /app
RUN apt update -y
# For building wsgi, we'll be needing c compiler on the system
RUN apt install gcc -y
RUN pip3 install --upgrade pip
ADD ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt 
RUN apt install curl -y
ADD . /app
CMD [ "python3","api.py" ]
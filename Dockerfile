FROM python:3

MAINTAINER Mahmoud Jbour "omarmahmmoud@gmail.com"
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 5000

CMD [ "python", "login_watcher.py" ]
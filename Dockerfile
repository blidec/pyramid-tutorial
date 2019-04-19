FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
    
RUN pip install --upgrade pip setuptools

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install -e ".[dev]"

CMD ["pserve", "development.ini", "--reload" ] 
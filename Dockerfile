FROM ubuntu:latest

MAINTAINER Prangya P Kar "prangya.kar@gmail.com"

#install required software in ubuntu container

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN echo "$PWD"

COPY textwrap.py ./


CMD ["python3", "./textwrap.py"]

# To Run:
# docker build -t prangya-text-wrap:1.0 . -f Dockerfile --no-cache
# docker run -it --name prangya-text-wrap prangya-text-wrap:1.0

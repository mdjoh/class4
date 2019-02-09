FROM ubuntu:16.04
MAINTAINER Marchiano Oh <github mdjoh>

RUN apt-get update
RUN apt-get install -y python3-pip

#RUN cat /etc/lsb/release

# example copying file
RUN mkdir -p /opt

COPY README.md /opt/README_new.md

FROM ubuntu:16.04
MAINTAINER Marchiano Oh <github mdjoh>

RUN apt-get update
RUN apt-get install -y python3-pip

#RUN cat /etc/lsb/release


# Update to python 3. Install: pip. Then install numpy, pandas using pip

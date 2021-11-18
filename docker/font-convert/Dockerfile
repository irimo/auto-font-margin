FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu16.04

ENV DEBIAN_FRONTEND=noninteractive

ARG python_version="3.7.3"


RUN mkdir /workspace
WORKDIR /workspace

RUN apt-get update

RUN apt-get install autoconf -y
RUN apt-get install automake -y
RUN apt-get install fontforge -y

WORKDIR /workspace
RUN apt-get install wget -y
RUN wget https://download.savannah.gnu.org/releases/freetype/freetype-2.10.1.tar.gz
RUN tar xvfz freetype-2.10.1.tar.gz
WORKDIR freetype-2.10.1
RUN ./configure --prefix=/usr/local/freetype/2_10_1 --enable-freetype-config
RUN make
RUN make install

RUN apt-get install imagemagick -y

WORKDIR /workspace
RUN apt-get install git -y
RUN git clone https://github.com/fontforge/libspiro
WORKDIR libspiro
RUN apt-get  install libtool -y
RUN autoreconf --install --force
RUN automake --foreign -Wall

RUN apt-get install m4 -y
RUN apt-get install potrace -y

RUN apt-get install python3 -y

WORKDIR /
RUN rm -rf workspace/


# Docker内で
WORKDIR /home
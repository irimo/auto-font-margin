FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu16.04

ENV DEBIAN_FRONTEND=noninteractive

ARG python_version="3.7.3"
ARG version="4.2.0"

# like tool
RUN apt-get update && apt-get -y upgrade &&\
    apt-get install -y --no-install-recommends \
    vim unzip byobu wget tree git cmake\
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# install python3.7.3
RUN apt-get update && apt-get install -y zlib1g-dev libssl-dev libffi-dev build-essential \
    checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev \
    libgdbm-dev libc6-dev libbz2-dev &&\
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN mkdir /workspace
WORKDIR /workspace

# install python3
RUN wget -c https://www.python.org/ftp/python/${python_version}/Python-${python_version}.tgz &&\
    tar zxvf Python-${python_version}.tgz && cd Python-${python_version} &&\
    ./configure --enable-optimizations --enable-shared CFLAGS=-fPIC &&\
    make -j8 && make install && ldconfig && cd .. && rm Python-${python_version}.tgz &&\
    rm -rf Python-${python_version}
RUN pip3 install -U pip
RUN pip3 install -U setuptools

RUN pip3 install -U ttfquery



WORKDIR /
RUN rm -rf workspace/


# Docker内で
WORKDIR /home
# syntax = docker/dockerfile:experimental@sha256:3c244c0c6fc9d6aa3ddb73af4264b3a23597523ac553294218c13735a2c6cf79
FROM ubuntu:20.04

WORKDIR /app

ARG DEBIAN_FRONTEND=noninteractive

# APT packages
RUN apt update && apt install -y curl wget python3 python3-distutils python3-venv git build-essential

# CMake
COPY build-scripts/install_cmake.sh ./
RUN /bin/bash install_cmake.sh && \
    rm install_cmake.sh

# Flatbuffer compiler
RUN cd /opt && \
    git clone https://github.com/google/flatbuffers.git && \
    cd flatbuffers && \
    git checkout 48da2389205ca5fbd0d1f40ad52d9c0b8685a076 && \
    cmake -G "Unix Makefiles" && \
    make -j$(nproc) && \
    ln -s $PWD/flatc /usr/local/bin/flatc

# Newer version of sed (https://forums.docker.com/t/sed-couldnt-open-temporary-file-xyz-permission-denied-when-using-virtiofs/125473/4)
RUN cd /opt && \
    wget ftp://ftp.gnu.org/gnu/sed/sed-4.8.tar.xz && \
    tar xf sed-4.8.tar.xz && \
    rm sed-4.8.tar.xz && \
    cd sed-4.8 && \
    ./configure && \
    make -j && \
    make install

# Pip
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py "pip==21.3.1" && \
    rm get-pip.py

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

# JDK relies on glibc
FROM docker.io/jeanblanchard/alpine-glibc
# author
LABEL maintainer="wei dong"
# A streamlined jre
ADD jre8.tar.gz /usr/java/jdk/
# set env
ENV JAVA_HOME /usr/java/jdk
ENV PATH ${PATH}:${JAVA_HOME}/bin
# run container with base path
WORKDIR /opt

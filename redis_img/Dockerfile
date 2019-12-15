FROM debian:stable
LABEL maintainer="wei dong"
ENV APP_DIR /usr/local
ENV RS_VERSION 5.0.7
ADD http://download.redis.io/releases/redis-${RS_VERSION}.tar.gz /
RUN mkdir -p ${APP_DIR}/redis && apt-get update && apt-get install build-essential -y

WORKDIR /redis-${RS_VERSION}
RUN make
RUN mv /redis-${RS_VERSION}/src/redis-server ${APP_DIR}/redis && mv /redis-${RS_VERSION}/redis.conf ${APP_DIR}/redis && rm -rf /redis-${RS_VERSION}

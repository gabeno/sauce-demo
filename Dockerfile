FROM ubuntu:focal-20210416

ENV DEBIAN_FRONTEND=noninteractive
ENV DOCKERIZE_VERSION v0.6.1

RUN apt-get -qqy update && apt-get -qqy upgrade
RUN apt-get -qqy --no-install-recommends install python3-pip wget
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
RUN pip3 install testcontainers[selenium] selenium ipython httpie pytest

COPY ./tests ./tests

CMD ["pytest", "tests"]

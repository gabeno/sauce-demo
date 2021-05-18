FROM ubuntu:bionic

ENV DEBIAN_FRONTEND=noninteractive
ENV DOCKERIZE_VERSION v0.6.1

RUN apt-get -qqy update && apt-get -qqy upgrade
RUN apt-get -qqy --no-install-recommends install python3-pip wget unzip libglib2.0-0 libnss3 libx11-6
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
RUN pip3 install selenium ipython httpie pytest
RUN wget -q "http://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip
RUN wget -q "https://msedgedriver.azureedge.net/91.0.864.1/edgedriver_linux64.zip" -O /tmp/edgedriver.zip \
    && unzip /tmp/edgedriver.zip -d /usr/bin/ \
    && rm /tmp/edgedriver.zip
RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz" -O /tmp/geckodriver.tgz \
    && tar zxf /tmp/geckodriver.tgz -C /usr/bin/ \
    && rm /tmp/geckodriver.tgz

COPY ./tests ./tests

CMD ["pytest", "tests"]

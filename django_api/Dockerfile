FROM python:2.7

ARG env
ENV ENV ${env:-dev}

ARG requirement_file
ENV REQUIREMENT_FILE ${requirement_file:-dev.txt}

# Install dependencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential \
    libcurl4-openssl-dev \
    libjpeg-dev \
    libgif-dev \
    libffi-dev \
    libpng-dev \
    libtiff-dev \
    libxml2-dev \
    libxslt-dev \
    xmlsec1 \
    vim \
    ntp
RUN apt-get install -y --no-install-recommends \
    git-core
RUN apt-get install -y --no-install-recommends \
    python-dev \
    python-software-properties \
    python-setuptools
RUN apt-get install -y --no-install-recommends \
    postgresql-client \
    libpq-dev \
    python-psycopg2
RUN apt-get install -y --no-install-recommends \
    python-gdal \
    gdal-bin \
    libgdal-dev \
    libgdal1h \
    libgdal1-dev

# Install Python tools
RUN pip install --upgrade \
    virtualenv \
    virtualenvwrapper \
    fabric \
    pip \
    wheel

# http://gis.stackexchange.com/a/74060
ENV CPLUS_INCLUDE_PATH /usr/include/gdal
ENV C_INCLUDE_PATH /usr/include/gdal

ADD ./requirements/* /tmp/

# Install PyPi dependencies
WORKDIR /tmp
RUN pip install -r $REQUIREMENT_FILE

ADD . /code/
VOLUME /code

RUN mkdir -p /data/django_api/logs
RUN touch /data/django_api/logs/django.log

VOLUME /data
RUN chmod -R a+rw /data

ENV PYTHONUNBUFFERED 1
WORKDIR /code/

COPY waitforit /usr/local/bin/waitforit
RUN chmod +x /usr/local/bin/waitforit

EXPOSE 8000

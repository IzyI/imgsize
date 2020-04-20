FROM debian:latest as builder
ARG tag=v3.3.1

RUN DEBIAN_FRONTEND="noninteractive" \
	apt-get update && \
	apt-get install --no-install-recommends --yes \
		automake \
		libpng-dev \
		libtool \
		make \
		nasm \
		pkg-config && \
	apt-get clean

WORKDIR /root/build
ADD https://github.com/mozilla/mozjpeg/archive/$tag.tar.gz ./
RUN tar -xzf $tag.tar.gz
RUN rm $tag.tar.gz


RUN SRC_DIR=$(ls -t1 -d mozjpeg-* | head -n1) && \
    cd $SRC_DIR && \
    autoreconf -fiv && \
    cd .. && \
    sh $SRC_DIR/configure && \
    make install \
         prefix=/usr/local \
         libdir=/usr/local/lib64


# imgsize
FROM debian:latest
RUN  apt-get clean && apt-get update &&	apt-get install --no-install-recommends --yes \
                    python3 optipng gifsicle python3-pil python3-pip python3-setuptools

RUN apt-get install -y locales

# Locale
RUN sed -i -e  's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen   && locale-gen
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8


COPY --from=builder /usr/local /usr/local
WORKDIR /root


# Python
ENV PYTHONUNBUFFERED 1
ADD ./requirements.txt /
RUN pip3 install wheel
RUN pip3 install -r /requirements.txt
    ADD ./test.py .
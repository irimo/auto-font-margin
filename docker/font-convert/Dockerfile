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

RUN apt-get install nginx -y
RUN nginx

WORKDIR /workspace
RUN wget -O init-deb.sh https://www.linode.com/docs/assets/660-init-deb.sh
RUN mv init-deb.sh /etc/init.d/nginx
RUN chmod +x /etc/init.d/nginx
RUN /usr/sbin/update-rc.d -f nginx defaults
RUN apt-get install php -y
RUN apt-get install php-fpm -y

# このへん作業用
RUN apt-get install vim -y
RUN apt-get install lsof -y

WORKDIR /
RUN rm -rf workspace/

COPY ./copy_files/php_setting.conf /etc/nginx/conf.d/

# Docker内で
RUN service nginx start
WORKDIR /var/www/html
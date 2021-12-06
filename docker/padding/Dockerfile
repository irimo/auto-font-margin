# FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu16.04
FROM php:7.0-apache
# ENV DEBIAN_FRONTEND=noninteractive

# ARG python_version="3.7.3"


RUN mkdir /workspace
# WORKDIR /workspace

RUN apt-get update
# RUN apt-get install -y wget git unzip libpq-dev libfreetype6-dev libjpeg62-turbo-dev libpng-dev
# RUN docker-php-ext-install -j$(nproc) pdo_pgsql
# RUN docker-php-ext-configure gd --with-freetype --with-jpeg
# RUN docker-php-ext-install -j$(nproc) gd
# RUN apt install -y ca-certificates
# RUN apt-get install autoconf -y
# RUN apt-get install automake -y
# RUN apt-get install fontforge -y

# WORKDIR /workspace

# FROM php:8.0.9-fpm-alpine

WORKDIR /workspace
RUN apt-get install wget -y
# RUN wget https://download.savannah.gnu.org/releases/freetype/freetype-2.10.1.tar.gz
COPY ./copy_files/src/freetype-2.10.1.tar.gz ./
RUN tar xvfz freetype-2.10.1.tar.gz
WORKDIR freetype-2.10.1
RUN ./configure --prefix=/usr/local/freetype/2_10_1 --enable-freetype-config
RUN make
RUN make install

WORKDIR /workspace
RUN apt-get install zlib1g-dev
RUN apt-get install -y git
RUN git clone https://github.com/glennrp/libpng.git
WORKDIR libpng
RUN ./configure && make && make install

WORKDIR /workspace
RUN apt-get install -y cmake
RUN git clone https://github.com/libjpeg-turbo/libjpeg-turbo.git
WORKDIR libjpeg-turbo
RUN mkdir build
WORKDIR build
RUN cmake .. -DCMAKE_INSTALL_PREFIX=/usr/local/libjpeg_turbo/2_0_2 -DCMAKE_BUILD_TYPE=RELEASE
RUN make
RUN make install

# RUN apt-get install -y libjpeg-turbo-dev
RUN docker-php-ext-configure gd -with-jpeg=/usr/include/ --with-freetype=/usr/include/
RUN NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1)
# RUN docker-php-ext-install -j${NPROC} gd pdo_mysql
# RUN apt remove freetype-dev libpng-dev libjpeg-turbo-dev

# COPY --from=composer:2.1 /usr/bin/composer /usr/bin/composer

# RUN { \
#   echo 'access.format = "%R - %u %t \"%m %{REQUEST_URI}e\" %s"'; \
# } >> /usr/local/etc/php-fpm.d/www.conf

RUN apt-get install imagemagick -y

# WORKDIR /workspace
# RUN apt-get install git -y
# RUN git clone https://github.com/fontforge/libspiro
# WORKDIR libspiro
# RUN apt-get  install libtool -y
# RUN autoreconf --install --force
# RUN automake --foreign -Wall

# RUN apt-get install m4 -y
# RUN apt-get install potrace -y

# RUN apt-get install python3 -y

# RUN apt-get install nginx -y
# RUN nginx

# WORKDIR /workspace
# RUN wget -O init-deb.sh https://www.linode.com/docs/assets/660-init-deb.sh
# RUN mv init-deb.sh /etc/init.d/nginx
# RUN chmod +x /etc/init.d/nginx
# RUN /usr/sbin/update-rc.d -f nginx defaults
# RUN apt-get install php -y

# RUN apt-get install apache2 -y
# RUN apt-get install php -y
# RUN apt-get install php-fpm -y

# python apache
# RUN pacman -S mod_wsgi

# このへん作業用
RUN apt-get install vim -y
RUN apt-get install lsof -y
RUN apt-get install bash -y

WORKDIR /
# RUN rm -rf workspace/

# COPY ./copy_files/php_setting.conf /etc/nginx/conf.d/

# Docker内で
# RUN service nginx start
# RUN systemctl enable apache2
# EXPOSE 80
WORKDIR /var/www/html
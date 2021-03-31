FROM php:7.2-fpm

RUN apt-get update \
    && apt-get install iputils-ping -y \
    && docker-php-ext-install mysqli && docker-php-ext-enable mysqli

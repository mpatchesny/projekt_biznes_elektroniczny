FROM prestashop/prestashop:1.7.8.7

COPY ./prestashop/html /var/www/html/
COPY ./apache2/sites-available/000-default.conf /etc/apache2/sites-available
COPY ./ssl/duzybiceps.crt /etc/ssl
COPY ./ssl/private/duzybiceps.key /etc/ssl/private

RUN chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html
RUN a2enmod ssl

WORKDIR /var/www/html

EXPOSE 80 443
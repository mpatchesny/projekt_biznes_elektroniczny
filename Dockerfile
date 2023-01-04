FROM prestashop/prestashop:1.7.8.7

COPY ./prestashop/html/admin123 /var/www/html
COPY ./prestashop/html/app /var/www/html
COPY ./prestashop/html/bin /var/www/html
COPY ./prestashop/html/classes /var/www/html
COPY ./prestashop/html/config /var/www/html
COPY ./prestashop/html/controllers /var/www/html
COPY ./prestashop/html/docs /var/www/html
COPY ./prestashop/html/download /var/www/html
COPY ./prestashop/html/img /var/www/html
COPY ./prestashop/html/js /var/www/html
COPY ./prestashop/html/localization /var/www/html
COPY ./prestashop/html/mails /var/www/html
COPY ./prestashop/html/modules /var/www/html
COPY ./prestashop/html/override /var/www/html
COPY ./prestashop/html/pdf /var/www/html
COPY ./prestashop/html/src /var/www/html
COPY ./prestashop/html/themes /var/www/html
COPY ./prestashop/html/tools /var/www/html
COPY ./prestashop/html/translations /var/www/html
COPY ./prestashop/html/upload /var/www/html
COPY ./prestashop/html/vendor /var/www/html
COPY ./prestashop/html/webservice /var/www/html
COPY ./prestashop/html/.htaccess /var/www/html
COPY ./prestashop/html/autoload.php /var/www/html
COPY ./prestashop/html/composer.lock /var/www/html
COPY ./prestashop/html/error500.html /var/www/html
COPY ./prestashop/html/images.inc.php /var/www/html
COPY ./prestashop/html/index.php /var/www/html
COPY ./prestashop/html/init.php /var/www/html
COPY ./prestashop/html/INSTALL.txt /var/www/html
COPY ./prestashop/html/robots.txt /var/www/html
COPY ./prestashop/html/LICENSES /var/www/html
COPY ./prestashop/html/Makefile /var/www/html
COPY ./prestashop/html/phpstan.neon.dist /var/www/html
COPY ./apache2/sites-available/000-default.conf /etc/apache2/sites-available
COPY ./ssl/duzybiceps.crt /etc/ssl
COPY ./ssl/private/duzybiceps.key /etc/ssl/private
COPY ./mysql/database_dump.sql /home
COPY ./mysql/presta_db_config.sql /home

RUN chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html
RUN a2enmod ssl

WORKDIR /var/www/html

EXPOSE 80 443
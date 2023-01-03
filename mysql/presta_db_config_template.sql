USE ${DB_NAME};
UPDATE ps_configuration SET value = NULL WHERE ps_configuration.id_configuration = 9;
UPDATE ps_shop_url SET domain = '${DOMAIN_NAME}:${LOCAL_HTTP}', domain_ssl = '${DOMAIN_NAME}:${LOCAL_HTTPS}' WHERE ps_shop_url.id_shop_url = 1;
UPDATE ps_configuration SET value = '${DOMAIN_NAME}:${LOCAL_HTTP}' WHERE ps_configuration.id_configuration = 229;
UPDATE ps_configuration SET value = '${DOMAIN_NAME}:${LOCAL_HTTPS}' WHERE ps_configuration.id_configuration = 230;
USE prestashop;
UPDATE ps_configuration SET value = NULL WHERE ps_configuration.id_configuration = 9;
UPDATE ps_shop_url SET domain = 'localhost:8080', domain_ssl = 'localhost:8443' WHERE ps_shop_url.id_shop_url = 1;
UPDATE ps_configuration SET value = 'localhost:8080' WHERE ps_configuration.id_configuration = 229;
UPDATE ps_configuration SET value = 'localhost:8443' WHERE ps_configuration.id_configuration = 230;
-- Trait "smak" -> do attributes
-- pozostałe traity, oprócz "Kod EAN", idą do features
--table:ps_product
INSERT INTO prestashop.ps_product (id_product, id_supplier, id_manufacturer, id_category_default, id_shop_default, id_tax_rules_group, on_sale, online_only, ean13, isbn, upc, mpn, ecotax, quantity, minimal_quantity, low_stock_threshold, low_stock_alert, price, wholesale_price, unity, unit_price_ratio, additional_shipping_cost, reference, supplier_reference, location, width, height, depth, weight, out_of_stock, additional_delivery_times, quantity_discount, customizable, uploadable_files, text_fields, active, redirect_type, id_type_redirected, available_for_order, available_date, show_condition, condition, show_price, indexed, visibility, cache_is_pack, cache_has_attachments, is_virtual, cache_default_attribute, date_add, date_upd, advanced_stock_management,  pack_stock_type, state, product_type)
VALUES (
    (SELECT MAX(id_product)+1 FROM prestashop.ps_product), -- id_product
    0, --id_supplier,
    2, --id_manufacturer,
    -- ostatnia kategoria
    (SELECT id_category FROM prestashop.ps_category_lang WHERE name = '{kategoria}' LIMIT 1), --id_category_default,
    1, --id_shop_default,
    1, --id_tax_rules_group,
    0, --on_sale,
    0, --online_only,
    NULL, --ean13,
    NULL, --isbn,
    NULL, --upc,
    NULL, --mpn,
    0.0, --ecotax,
    300, --quantity,
    1, --minimal_quantity,
    NULL, --low_stock_threshold,
    false, --low_stock_alert,
    '{cena_netto}', --price, minus 23%
    0.0 --wholesale_price,
    NULL, --unity,
    0.0, --unit_price_ratio,
    0.0, --additional_shipping_cost,
    '{ean}', --reference, 
    NULL, --supplier_reference,
    NULL, --location,
    0.0, --width,
    0.0, --height,
    0.0, --depth,
    0.0, --weight,
    2, --out_of_stock,
    1, --additional_delivery_times,
    false, --quantity_discount,
    0, --customizable,
    0, --uploadable_files,
    0, --text_fields,
    1, --active,
    '301-category', --redirect_type,
    0, --id_type_redirected,
    TRUE, --available_for_order,
    NULL, --available_date,
    false, --show_condition,
    'new', --condition,
    true, --show_price,
    true, --indexed,
    'both', --visibility,
    false, --cache_is_pack,
    false, --cache_has_attachments,
    false, --is_virtual,
    40, --cache_default_attribute,
    (SELECT NOW() FROM dual), --date_add,
    (SELECT NOW() FROM dual), --date_upd,
    false, --advanced_stock_management,
    3, --pack_stock_type,
    1, --state,
    '{product_type}' --product_type
);
--table:ps_product_lang
INSERT INTO prestashop.ps_product_lang(id_product, id_shop, id_lang, description, description_short, link_rewrite, meta_description, meta_keywords, meta_title, name, available_now, available_later, delivery_in_stock, delivery_out_stock) 
VALUES (
    (SELECT MAX(id_product) FROM prestashop.ps_product),
    1,
    1,
    NULL,
    '<p>{opis}</p>',
    NULL, --link_rewrite
    NULL, 
    NULL,
    NULL, -- meta_title
    '{nazwa}',
    NULL,
    NULL,
    NULL,
    NULL
);
--table:ps_product_shop
INSERT INTO prestashop.ps_product_shop(id_product, id_shop, id_category_default, id_tax_rules_group, on_sale, online_only, ecotax, minimal_quantity, low_stock_threshold, low_stock_alert, price, wholesale_price, unity, unit_price_ratio, additional_shipping_cost, customizable, uploadable_files, text_fields, active, redirect_type, id_type_redirected, available_for_order, available_date, show_condition, condition, show_price, indexed, visibility, cache_default_attribute, advanced_stock_management, date_add, date_upd, pack_stock_type)
VALUES (
    (SELECT MAX(id_product) FROM prestashop.ps_product), -- id_product
    1, -- id_shop
    (SELECT id_category FROM prestashop.ps_category_lang WHERE name = '{kategoria}' LIMIT 1), -- id_category_default
    1, -- id_tax_rules_group
    0, -- on_sale
    0, -- online_only
    0.0, -- ecotax
    1, -- minimal_quantity
    NULL, -- low_stock_threshold
    false, -- low_stock_alert
     '{cena_netto}', -- price
    0.0, -- wholesale_price
    NULL, -- unity
    0.0, -- unit_price_ratio
    0.0, -- additional_shipping_cost
    0, -- customizable
    0, -- uploadable_files
    0, -- text_fields
    1, -- active
    '301-category', -- redirect_type
    0, -- id_type_redirected
    true, -- available_for_order
    NULL, -- available_date
    false, -- show_condition
    'new', -- condition
    true, -- show_price
    true, -- indexed
    'both', -- visibility
    40, -- cache_default_attribute
    false, -- advanced_stock_management
    (SELECT NOW() FROM dual), -- date_add
    (SELECT NOW() FROM dual), -- date_upd
    3, -- pack_stock_type
);
--table:ps_product_attribute
INSERT INTO prestashop.ps_product_attribute(id_product, id_product_attribute, reference, supplier_reference, location, ean13, isbn, upc, mpn, wholesale_price, price, ecotax, quantity, weight, unit_price_impact, default_on, minimal_quantity, low_stock_threshold, low_stock_alert, available_date)
VALUES (
    (SELECT MAX(id_product) FROM prestashop.ps_product), -- id_product
    (SELECT MAX(id_product_attribute)+1 FROM prestashop.ps_product_attribute), --id_product_attribute
    NULL, --reference
    NULL, --supplier_reference
    NULL, --location
    NULL, --ean13
    NULL, --isbn
    NULL, --upc
    NULL, --mpn
    0.0, --wholesale_price
    0.0, --price
    0.0, --ecotax
    300, --quantity
    0.0, --weight
    0.0, --unit_price_impact
    1, --default_on
    1, --minimal_quantity
    NULL, --low_stock_threshold
    false, --low_stock_alert
    NULL, --available_date
);
--table:ps_product_attribute_combination
INSERT INTO prestashop.ps_product_attribute_combination(id_attribute, id_product_attribute)
VALUES (
    (SELECT id_attribute FROM prestashop.ps_attribute_lang WHERE name = '{atrybut'),
    (SELECT MAX(id_product_attribute) FROM prestashop.ps_product_attribute)
);
--table:ps_product_attribute_shop
INSERT INTO prestashop.ps_product_attribute_shop (id_product, id_shop, id_category_default, id_tax_rules_group, on_sale, online_only, ecotax, minimal_quantity, low_stock_threshold, low_stock_alert, price, wholesale_price, unity, unit_price_ratio, additional_shipping_cost, customizable, uploadable_files, text_fields, active, redirect_type, id_type_redirected, available_for_order, available_date, show_condition, condition, show_price, indexed, visibility, cache_default_attribute, advanced_stock_management, date_add, date_upd, pack_stock_type)
VALUES (
    (SELECT MAX(id_product) FROM prestashop.ps_product), -- id_product
    1, --id_shop, 
    (SELECT id_category FROM prestashop.ps_category_lang WHERE name = '{kategoria}' LIMIT 1), -- id_category_default
    1, --id_tax_rules_group, 
    0, --on_sale, 
    0, --online_only, 
    0.0, --ecotax, 
    1, --minimal_quantity, 
    NULL, --low_stock_threshold, 
    false, --low_stock_alert, 
    '{cena_netto}', --price, 
    0.0, --wholesale_price, 
    NULL, --unity, 
    0.0, --unit_price_ratio, 
    0.0, --additional_shipping_cost, 
    0, --customizable, 
    0, --uploadable_files, 
    0, --text_fields, 
    1, --active, 
    '301-category', --redirect_type, 
    0, --id_type_redirected, 
    true, --available_for_order, 
    NULL, --available_date, 
    false, --show_condition, 
    'new', --condition, 
    true, --show_price, 
    true, --indexed, 
    'both', --visibility, 
    40, --cache_default_attribute, 
    false, --advanced_stock_management, 
    (SELECT NOW() FROM dual), -- date_add
    (SELECT NOW() FROM dual), -- date_upd
    3, -- pack_stock_type
);
--table:ps_feature_value_lang
INSERT INTO prestashop.ps_feature_value_lang(id_feature_value, id_lange, value)
VALUES (
    (SELECT MAX(id_feature_value)+1 FROM prestashop.ps_feature_value_lang),
    1,
    '{cecha}'
);
--table:ps_feature_product
INSERT INTO prestashop.ps_feature_product(id_feature, id_product, id_feature_value)
VALUES (
    (SELECT MAX(id_feature)+1 FROM prestashop.ps_feature_product), -- id_feature
    (SELECT MAX(id_product) FROM prestashop.ps_product), -- id_product
    (SELECT id_feature_value FROM prestashop.ps_feature_product WHERE value = '{cecha}') -- id_feature_value
);
-- /img/p/2/4/24.jpg
-- jak wstawić obrazek do dockera? ...
--table:ps_image
INSERT INTO prestashop.ps_image(id_imdage, id_product, position, cover) 
VALUES (
    TODO, -- id_image
    (SELECT MAX(id_product) FROM prestashop.ps_product), -- id_product
    1, 
    1
);
--table:ps_image_lang
INSERT INTO prestashop.ps_image_lang(id_image, id_lang, legend) 
VALUES (
    TODO, -- id_image
    1, 
    NULL
);
--table:ps_image_shop
INSERT INTO prestashop.ps_image_shop(id_product, id_image, id_shop, cover) 
VALUES (
    (SELECT MAX(id_product) FROM prestashop.ps_product), -- id_product
    TODO, -- id_image
    1, 
    1
);
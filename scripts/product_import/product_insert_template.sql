--table:ps_product
SET @newProductId := (SELECT COALESCE(MAX(id_product)+1, 1) FROM prestashop.ps_product);
INSERT INTO prestashop.ps_product
VALUES (
    @newProductId 
    , -- id_product
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
    0.0, --wholesale_price,
    NULL, --unity,
    0.0, --unit_price_ratio,
    0.0, --additional_shipping_cost,
    '{ean}', --reference, 
    NULL, --supplier_reference,
    'Magazyn domyślny', --location,
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
    -- FIXME: nie moze byc pusty
    NULL
);

--table:ps_product_lang
INSERT INTO prestashop.ps_product_lang
VALUES (
    (SELECT MAX(id_product) FROM prestashop.ps_product),
    1,
    1,
    NULL,
    '<p>{opis}</p>',
    '{link}', --link_rewrite
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
INSERT INTO prestashop.ps_product_shop
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
    3 -- pack_stock_type
);

--table:ps_product_attribute
SET @newProdAttrtibId := (SELECT COALESCE(MAX(id_product_attribute)+1, 1) FROM prestashop.ps_product_attribute);
INSERT INTO prestashop.ps_product_attribute
VALUES (
    (SELECT MAX(id_product) FROM prestashop.ps_product), -- id_product
    @newProdAttrtibId, --id_product_attribute
    NULL, --reference
    NULL, --supplier_reference
    'Magazyn domyślny', --location
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
    NULL --available_date
);

--table:ps_product_attribute_combination
INSERT INTO prestashop.ps_product_attribute_combination(id_attribute, id_product_attribute)
VALUES (
    (SELECT id_attribute FROM prestashop.ps_attribute_lang WHERE name = '{atrybut_wartosc}' LIMIT 1),
    (SELECT MAX(id_product_attribute) FROM prestashop.ps_product_attribute)
);

--table:ps_product_attribute_shop
INSERT INTO prestashop.ps_product_attribute_shop
VALUES (
    (SELECT MAX(id_product) FROM prestashop.ps_product), -- id_product
    (SELECT MAX(id_product_attribute) FROM prestashop.ps_product_attribute), --id_product_attribute
    1,
    0.0, --wholesale_price
    0.0, --price
    0.0, --ecotax
    0.0, --weight
    0.0, --unit_price_impact
    1, --default_on
    1, --minimal_quantity
    NULL, --low_stock_threshold
    false, --low_stock_alert
    NULL --available_date
);

--table:ps_feature_value_lang
SET @featureValueId := (SELECT COALESCE(MAX(id_feature_value)+1, 1) FROM prestashop.ps_feature_value_lang);
INSERT INTO prestashop.ps_feature_value_lang(id_feature_value, id_lang, value)
VALUES (
    @featureValueId,
    1,
    '{wartosc_cechy}'
);

--table:ps_feature_value
INSERT INTO prestashop.ps_feature_value(id_feature_value, id_feature, custom)
VALUES (
    (SELECT MAX(id_feature_value) FROM prestashop.ps_feature_value_lang),
    (SELECT id_feature FROM prestashop.ps_feature_lang WHERE name ='{nazwa_cechy}' LIMIT 1), -- id_feature
    1
);

--table:ps_feature_product
INSERT INTO prestashop.ps_feature_product(id_feature, id_product, id_feature_value)
VALUES (
    (SELECT id_feature FROM prestashop.ps_feature_lang WHERE name ='{nazwa_cechy}' LIMIT 1), -- id_feature
    (SELECT MAX(id_product) FROM prestashop.ps_product), -- id_product
    (SELECT MAX(id_feature_value) FROM prestashop.ps_feature_value_lang) -- id_feature_value
);

--table:ps_image
UPDATE prestashop.ps_image SET id_product=(SELECT MAX(id_product) FROM prestashop.ps_product), position=1, cover=1 WHERE id_image={image_id};

--table:ps_image_shop
UPDATE prestashop.ps_image_shop SET id_product=(SELECT MAX(id_product) FROM prestashop.ps_product), id_shop=1, cover=1 WHERE id_image={image_id};

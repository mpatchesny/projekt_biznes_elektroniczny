#! python3

# Skrypt, który tworzy plik SQL do importu produktów do bazy danych

import os
import sys
import json

def replacePolishDiacritics(text):
    polish = "ęółśążźćń"
    latin = "eolsazzcn"
    for i in range(0, len(polish)):
        text = text.replace(polish[i], latin[i])
    return text

def getLink(txt) -> str:
    url = str(txt.lower().replace(" ", "-"))
    url = replacePolishDiacritics(url)
    url = url.replace(",", "")
    url = url.replace("'", "")
    url = url.replace(".", "")
    url = url.replace("/", "-")
    return url

def generateQueryForProduct(product) -> str:
    """ Generuje zapytanie dla tabel dotyczących produktów """
    cena_netto = 0.0
    cena_brutto = product["price"]
    cena_brutto = cena_brutto.replace(" zł", "")
    cena_brutto = cena_brutto.replace(",", ".")
    cena_brutto = float(cena_netto)

    ean = product["ean"]
    category =  product["category"][0]
    queryProd = "SET @newProductId := (SELECT COALESCE(MAX(id_product)+1, 1) FROM prestashop.ps_product);"
    queryProd = queryProd+ f"""INSERT INTO prestashop.ps_product VALUES (@newProductId, 0, 2, (SELECT id_category FROM prestashop.ps_category_lang WHERE name = '{category}' LIMIT 1), 1, 1, 0, 0, NULL, NULL, NULL, NULL, 0.0, 300, 1, NULL, false, '{cena_netto}', '{cena_brutto}', NULL, 0.0, 0.0, '{ean}', NULL, 'Magazyn', 0.0, 0.0, 0.0, 0.0, 2, 1, false, 0, 0, 0, 1, '301-category', 0, TRUE, NULL, false, 'new', true, true, 'both', false, false, false, 0, (SELECT NOW() FROM dual), (SELECT NOW() FROM dual), false, 3, 1, 'pack');"""

    name = product["name"]
    description = product["description"]
    link = getLink(name)
    queryProdLang = f"""INSERT INTO prestashop.ps_product_lang VALUES ((SELECT MAX(id_product) FROM prestashop.ps_product), 1, 1, NULL, '<p>{description}</p>', '{link}', NULL, NULL, NULL, '{name}', NULL, NULL, NULL, NULL); """

    queryProdShop = f"""INSERT INTO prestashop.ps_product_shop VALUES ((SELECT MAX(id_product) FROM prestashop.ps_product), 1, (SELECT id_category FROM prestashop.ps_category_lang WHERE name = '{category}' LIMIT 1), 1, 0, 0, 0.0, 1, NULL, false, '{cena_netto}', '{cena_brutto}', NULL, 0.0, 0.0, 0, 0, 0, 1, '301-category', 0, true, NULL, false, 'new', true, true, 'both', 0, false, (SELECT NOW() FROM dual), (SELECT NOW() FROM dual), 3);"""

    queryProdStock = f"""SET @newStockAId := (SELECT COALESCE(MAX(id_stock_available)+1, 1) FROM prestashop.ps_stock_available);\n
    INSERT INTO prestashop.ps_stock_available VALUES (@newStockAId, (SELECT MAX(id_product) FROM prestashop.ps_product), 0, 1, 0, 300, 300, 0, 0, 0, 'Magazyn');"""

    return queryProd + "\n" + queryProdLang + "\n" + queryProdShop+  "\n" + queryProdStock

def generateQueryForProductCategories(product) -> str:
    """ Generuje zapytanie dla tabel dotyczących kategorii produktów """
    li = []
    i = 1
    for x in product["category"]:
        category = x
        query = f"""INSERT INTO prestashop.ps_category_product VALUES ((SELECT id_category FROM prestashop.ps_category_lang WHERE name = '{category}' LIMIT 1), (SELECT MAX(id_product) FROM prestashop.ps_product), {i});"""
        li.append(query)
        i += 1
    return "\n".join(li)

def generateQueryForProductFeatures(product) -> str:
    """ Generuje zapytanie dla tabel dotyczących funkcje produktów """
    li = []
    for x in product["features"]:
        for key in x.keys():
            feature_name = key[:-1]
            feature_value = x[key]

            query1 = f"""SET @featureValueId := (SELECT COALESCE(MAX(id_feature_value)+1, 1) FROM prestashop.ps_feature_value_lang);\n
            INSERT INTO prestashop.ps_feature_value_lang(id_feature_value, id_lang, value)
            VALUES (@featureValueId, 1, '{feature_value}');"""

            query2 = f"""INSERT INTO prestashop.ps_feature_value(id_feature_value, id_feature, custom) VALUES ((SELECT id_feature_value FROM prestashop.ps_feature_value_lang WHERE value ='{feature_value}' ORDER BY id_feature_value DESC LIMIT 1), (SELECT id_feature FROM prestashop.ps_feature_lang WHERE name ='{feature_name}' ORDER BY id_feature DESC LIMIT 1), 1);"""

            query3 = f"""INSERT INTO prestashop.ps_feature_product(id_feature, id_product, id_feature_value)
            VALUES ((SELECT id_feature FROM prestashop.ps_feature_lang WHERE name ='{feature_name}' ORDER BY id_feature DESC LIMIT 1), (SELECT MAX(id_product) FROM prestashop.ps_product),(SELECT id_feature_value FROM prestashop.ps_feature_value_lang WHERE value ='{feature_value}' ORDER BY id_feature_value DESC LIMIT 1));"""

            li.append(query1)
            li.append(query2)
            li.append(query3)
    "\n".join(li)

def generateQueryForProductAttributes(product) -> str:
    """ Generuje zapytanie dla tabel dotyczących atrybutów produktów """
    li = []
    for x in product["attributes"]:
        for key in x.keys():
            attribute_name = key[:-1]
            attribute_value = x[key]
            is_default = 1

            prodAttribute = f"""SET @newProdAttrtibId := (SELECT COALESCE(MAX(id_product_attribute)+1, 1) FROM prestashop.ps_product_attribute);\n
            INSERT INTO prestashop.ps_product_attribute VALUES ((SELECT MAX(id_product) FROM prestashop.ps_product), @newProdAttrtibId, NULL, NULL, 'Magazyn', NULL, NULL, NULL, NULL, 0.0, 0.0, 0.0, 300, 0.0, 0.0, {is_default}, 1, NULL, false, NULL);"""

            prodAttribCombination = f"""INSERT INTO prestashop.ps_product_attribute_combination(id_attribute, id_product_attribute) VALUES ((SELECT id_attribute FROM prestashop.ps_attribute_lang WHERE name = '{attribute_value}' LIMIT 1), (SELECT MAX(id_product_attribute) FROM prestashop.ps_product_attribute));"""

            prodAttributeShop = f"""INSERT INTO prestashop.ps_product_attribute_shop VALUES ((SELECT MAX(id_product) FROM prestashop.ps_product), (SELECT MAX(id_product_attribute) FROM prestashop.ps_product_attribute), 1, 0.0, 0.0, 0.0, 0.0, 0.0, {is_default}, 1, NULL, false, NULL);"""

            stockAvailable = f"""SET @newStockAId := (SELECT COALESCE(MAX(id_stock_available)+1, 1) FROM prestashop.ps_stock_available);\n
            INSERT INTO prestashop.ps_stock_available VALUES (@newStockAId, (SELECT MAX(id_product) FROM prestashop.ps_product), (SELECT MAX(id_product_attribute) FROM prestashop.ps_product_attribute), 1, 0, 300, 300, 0, 0, 0, 'Magazyn');"""

            li.append(prodAttribute, prodAttribCombination, prodAttributeShop, stockAvailable)

            if (is_default == 1): is_default == 0

def generateQueryForProductImage(product) -> str:
    """ Generuje zapytanie dla tabel dotyczących obrazków produktów """
    image_id = product["image_id"]
    query1 = f"UPDATE prestashop.ps_image SET id_product = (SELECT MAX(id_product) FROM prestashop.ps_product), position=1, cover=1 WHERE id_image={image_id};"
    query2 = f"UPDATE prestashop.ps_image_shop SET id_product = (SELECT MAX(id_product) FROM prestashop.ps_product), id_shop=1, cover=1 WHERE id_image={image_id};"
    return query1 + "\n" + query2

def generateQueryForProduct(product) -> list:
    li = []
    functions = [generateQueryForProduct, generateQueryForProductCategories, generateQueryForProductFeatures, generateQueryForProductAttributes,generateQueryForProductImage]
    for func in functions:
        sql = func(product)
        if sql:
            li.append(sql)
    return li

def generateQuery(scrapData, queryTemplate) -> list:
    li = []
    li.append("SET AUTOCOMMIT = 0;")
    li.append("START TRANSACTION;")

    for prod in scrapData:
        sql = generateQueryForProduct(prod)

        name = prod["name"]
        li.append("/*" + (98 * "*"))
        li.append(name)
        li.append((98 * "*") + "*/")
        li.append(f"SELECT '{name}';")

        for x in sql:
            li.append(x)
        # *** DEBUG ***
        # break

    li.append("COMMIT;")
    return li

def main(argv):
    with open(argv[0], "r", encoding="utf-8") as f:
        scrapData = json.loads(f.read())
        
        with open(argv[1], "r", encoding="utf-8") as f2:
            queryTemplate = f2.read()
            sql = generateQuery(scrapData, queryTemplate)

            with open("INSERT_PRODUCTS.sql", "w", encoding="utf-8") as f3:
                f3.write("\n".join(sql))

main(sys.argv[1:])
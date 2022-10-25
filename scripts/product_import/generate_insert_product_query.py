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
    url = url.replace("+", "-")
    url = url.replace("/", "-")
    return url

def generateQueryForProduct(product) -> str:
    """ Generuje zapytanie dla tabel dotyczących produktów """
    cena_netto = product["price"]
    cena_netto = cena_netto.replace(" zł", "")
    cena_netto = cena_netto.replace(",", ".")
    cena_netto = round(float(cena_netto) / (1.23), 2)

    ean = product.get("ean")
    category =  product["category"][0]
    queryProd = "SET @newProductId := (SELECT COALESCE(MAX(id_product)+1, 1) FROM prestashop.ps_product);\n"
    queryProd = queryProd+ f"""INSERT INTO prestashop.ps_product VALUES (@newProductId, 0, 2, (SELECT id_category FROM prestashop.ps_category_lang WHERE name = '{category}' LIMIT 1), 1, 1, 0, 0, NULL, NULL, NULL, NULL, 0.0, 300, 1, NULL, false, '{cena_netto}', 0.0, NULL, 0.0, 0.0, '{ean}', NULL, 'Magazyn', 0.0, 0.0, 0.0, 0.0, 2, 1, false, 0, 0, 0, 1, '301-category', 0, TRUE, NULL, false, 'new', true, true, 'both', false, false, false, 0, (SELECT NOW() FROM dual), (SELECT NOW() FROM dual), false, 3, 1, 'pack');"""

    name = product["name"]
    name = name.replace("'", "''")
    description = product["description"]
    description = description.replace("'", "''")
    link = getLink(name)
    queryProdLang = f"""INSERT INTO prestashop.ps_product_lang VALUES ((SELECT MAX(id_product) FROM prestashop.ps_product), 1, 1, NULL, '<p>{description}</p>', '{link}', NULL, NULL, NULL, '{name}', NULL, NULL, NULL, NULL); """

    queryProdShop = f"""INSERT INTO prestashop.ps_product_shop VALUES ((SELECT MAX(id_product) FROM prestashop.ps_product), 1, (SELECT id_category FROM prestashop.ps_category_lang WHERE name = '{category}' LIMIT 1), 1, 0, 0, 0.0, 1, NULL, false, '{cena_netto}', 0.0, NULL, 0.0, 0.0, 0, 0, 0, 1, '301-category', 0, true, NULL, false, 'new', true, true, 'both', 0, false, (SELECT NOW() FROM dual), (SELECT NOW() FROM dual), 3);"""

    queryProdStock = f"""SET @newStockAId := (SELECT COALESCE(MAX(id_stock_available)+1, 1) FROM prestashop.ps_stock_available);\nINSERT INTO prestashop.ps_stock_available VALUES (@newStockAId, (SELECT MAX(id_product) FROM prestashop.ps_product), 0, 1, 0, 300, 300, 0, 0, 0, 'Magazyn');"""

    return queryProd + "\n" + queryProdLang + "\n" + queryProdShop+  "\n" + queryProdStock

def generateQueryForProductCategories(product) -> str:
    """ Generuje zapytanie dla tabel dotyczących kategorii produktów """
    i = 1
    li = []
    name = product["name"]
    name = name.replace("'", "''")

    category = 'Strona główna'
    query = f"""INSERT IGNORE INTO prestashop.ps_category_product VALUES ((SELECT id_category FROM prestashop.ps_category_lang WHERE name = '{category}' LIMIT 1),(SELECT id_product FROM prestashop.ps_product_lang WHERE name='{name}' LIMIT 1), {i});"""
    i += 1
    li.append(query)

    for x in product["category"]:
        category = x
        query = f"""INSERT IGNORE INTO prestashop.ps_category_product VALUES ((SELECT id_category FROM prestashop.ps_category_lang WHERE name = '{category}' LIMIT 1), (SELECT id_product FROM prestashop.ps_product_lang WHERE name='{name}' LIMIT 1), {i});"""
        li.append(query)
        i += 1
    return "\n".join(li)

def generateQueryForProductFeatures(product) -> str:
    """ Generuje zapytanie dla tabel dotyczących funkcje produktów """
    if not product.get("features"):
        return

    li = []
    for x in product["features"]:
        for key in x.keys():
            if not (key in ["Rodzaj", "Smak", "Rodzaj shota", "Kolor", "Rodzaj:", "Smak:", "Rodzaj shota:", "Kolor:"]):
                feature_name = key
                feature_name = feature_name.replace("'", "''")
                feature_value = x[key]
                feature_value = feature_value.replace("'", "''")

                query1 = f"""SET @featureValueId := (SELECT COALESCE(MAX(id_feature_value)+1, 1) FROM prestashop.ps_feature_value_lang);\nINSERT INTO prestashop.ps_feature_value_lang(id_feature_value, id_lang, value) VALUES (@featureValueId, 1, '{feature_value}');"""

                query2 = f"""INSERT INTO prestashop.ps_feature_value(id_feature_value, id_feature, custom) VALUES ((SELECT id_feature_value FROM prestashop.ps_feature_value_lang WHERE value ='{feature_value}' ORDER BY id_feature_value DESC LIMIT 1), (SELECT id_feature FROM prestashop.ps_feature_lang WHERE name ='{feature_name}' ORDER BY id_feature DESC LIMIT 1), 1);"""

                query3 = f"""INSERT INTO prestashop.ps_feature_product(id_feature, id_product, id_feature_value) VALUES ((SELECT id_feature FROM prestashop.ps_feature_lang WHERE name ='{feature_name}' ORDER BY id_feature DESC LIMIT 1), (SELECT MAX(id_product) FROM prestashop.ps_product),(SELECT id_feature_value FROM prestashop.ps_feature_value_lang WHERE value ='{feature_value}' ORDER BY id_feature_value DESC LIMIT 1));"""

                li.append(query1)
                li.append(query2)
                li.append(query3)
    return "\n".join(li)

def generateQueryForProductAttributes(product) -> str:
    """ Generuje zapytanie dla tabel dotyczących atrybutów produktów """
    li = []
    if not product.get("attributes"):
        return

    is_default = "1"
    for x in product["attributes"]:
        for key in x.keys():
            if not key in ["Liczba sztuk:", "Opór:"]:
                attribute_name = key[:-1]
                attribute_name = attribute_name.replace("'", "''")
                attribute_value = x[key]
                attribute_value = attribute_value.replace("'", "''")

                prodAttributeLookup = f"""INSERT INTO prestashop.ps_attribute_lang SELECT (SELECT COALESCE(MAX(id_attribute)+1, 1) FROM prestashop.ps_attribute_lang), 1, '{attribute_value}' FROM DUAL WHERE NOT EXISTS (SELECT * FROM prestashop.ps_attribute_lang WHERE name='{attribute_value}' LIMIT 1);\nINSERT INTO prestashop.ps_attribute SELECT (SELECT id_attribute FROM prestashop.ps_attribute_lang WHERE name='{attribute_value}' LIMIT 1), (SELECT id_attribute_group FROM prestashop.ps_attribute_group_lang WHERE name='{attribute_name}' LIMIT 1), 'color', 0 FROM DUAL WHERE NOT EXISTS (SELECT * FROM prestashop.ps_attribute WHERE id_attribute = (SELECT id_attribute FROM prestashop.ps_attribute_lang WHERE name='{attribute_value}' LIMIT 1) LIMIT 1);"""

                prodAttribute = f"""SET @newProdAttrtibId := (SELECT COALESCE(MAX(id_product_attribute)+1, 1) FROM prestashop.ps_product_attribute);\nINSERT INTO prestashop.ps_product_attribute VALUES (@newProdAttrtibId, (SELECT MAX(id_product) FROM prestashop.ps_product), NULL, NULL, 'Magazyn', NULL, NULL, NULL, NULL, 0.0, 0.0, 0.0, 300, 0.0, 0.0, {is_default}, 1, NULL, false, NULL);"""

                prodAttribCombination = f"""INSERT INTO prestashop.ps_product_attribute_combination(id_attribute, id_product_attribute) VALUES ((SELECT id_attribute FROM prestashop.ps_attribute_lang WHERE name = '{attribute_value}' LIMIT 1), (SELECT MAX(id_product_attribute) FROM prestashop.ps_product_attribute));"""

                prodAttributeShop = f"""INSERT INTO prestashop.ps_product_attribute_shop VALUES ((SELECT MAX(id_product) FROM prestashop.ps_product), (SELECT MAX(id_product_attribute) FROM prestashop.ps_product_attribute), 1, 0.0, 0.0, 0.0, 0.0, 0.0, {is_default}, 1, NULL, false, NULL);"""

                stockAvailable = f"""SET @newStockAId := (SELECT COALESCE(MAX(id_stock_available)+1, 1) FROM prestashop.ps_stock_available);\nINSERT INTO prestashop.ps_stock_available VALUES (@newStockAId, (SELECT MAX(id_product) FROM prestashop.ps_product), (SELECT MAX(id_product_attribute) FROM prestashop.ps_product_attribute), 1, 0, 300, 300, 0, 0, 0, 'Magazyn');"""

                li.append(prodAttributeLookup)
                li.append(prodAttribute)
                li.append(prodAttribCombination)
                li.append(prodAttributeShop)
                li.append(stockAvailable)
                li.append("\n")

                if (is_default == "1"): is_default = "NULL"

    return "\n".join(li)

def generateQueryForProductImage(product) -> str:
    """ Generuje zapytanie dla tabel dotyczących obrazków produktów """
    image_id = product["image_id"]
    query1 = f"UPDATE prestashop.ps_image SET id_product = (SELECT MAX(id_product) FROM prestashop.ps_product), position=1, cover=1 WHERE id_image={image_id};"
    query2 = f"UPDATE prestashop.ps_image_shop SET id_product = (SELECT MAX(id_product) FROM prestashop.ps_product), id_shop=1, cover=1 WHERE id_image={image_id};"
    return query1 + "\n" + query2

def generateQueryForOneProduct(product) -> list:
    li = []
    # functions = [generateQueryForProduct, generateQueryForProductCategories, generateQueryForProductFeatures, generateQueryForProductAttributes, generateQueryForProductImage]
    functions = [generateQueryForProductCategories]
    for func in functions:
        sql = func(product)

        if sql:
            li.append(f"/* {func} */")
            li.append(sql)
    return li

def generateQuery(scrapData) -> list:
    li = []
    li.append("SET AUTOCOMMIT = 0;")
    li.append("START TRANSACTION;")

    for prod in scrapData:
        sql = generateQueryForOneProduct(prod)

        name = prod["name"]
        li.append("/*" + (98 * "*"))
        li.append(name)
        li.append((98 * "*") + "*/")
        li.append(f"SELECT '{name}';")

        for x in sql:
            li.append(x)
        # *** DEBUG ***
        # break

    li.append("\nCOMMIT;")
    return li

def main(argv):
    with open(argv[0], "r", encoding="utf-8") as f:
        scrapData = json.loads(f.read())
        sql = generateQuery(scrapData)
        with open("INSERT_PRODUCTS.sql", "w", encoding="utf-8") as f2:
            f2.write("\n".join(sql))

main(sys.argv[1:])
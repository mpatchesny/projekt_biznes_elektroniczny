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
    url = url.replace("+", "-")
    url = url.replace("--", "-")
    url = url.replace("--", "-")
    return url

def replaceBasicValues(product, templateCopy) -> str:
    cena = product["price"]
    cena = cena.replace(" zł", "")
    cena = cena.replace(",", ".")
    cena = float(cena)
    cena = cena * (1-0.23)
    cena = round(cena, 3)
    templateCopy = templateCopy.replace("{cena_netto}", str(cena))

    kategoria = product["category"][-1]
    templateCopy = templateCopy.replace("{kategoria}", kategoria)

    ean = "" # random
    for x in product["traits"]:
        if x.get("Kod EAN:"):
            ean = x.get("Kod EAN:")
    templateCopy = templateCopy.replace("{ean}", ean)
    templateCopy = templateCopy.replace("{nazwa}", product["name"].strip().replace("'", "''"))
    templateCopy = templateCopy.replace("{link}", getLink(product["name"].strip()))
    templateCopy = templateCopy.replace("{product_type}", "3")
    templateCopy = templateCopy.replace("{opis}", product["description"].replace("'", "''"))
    templateCopy = templateCopy.replace("{image_id}", str(product["image_id"]))
    return templateCopy

def generateQueryForCategories(product, template) -> list:
    li = []
    i = 1
    for x in product["category"]:
        templateCopy = template[:]
        templateCopy = templateCopy.replace("{kategoria}", x)
        templateCopy = templateCopy.replace("{i}", str(i))
        li.append(templateCopy)
        i += 1
    return li

def generateQueryForAttribs(product, template) -> list:
    for x in product["traits"]:
        for key in x.keys():
            if key == "Smak:":
                templateCopy = template[:]
                templateCopy = replaceBasicValues(product, templateCopy)
                templateCopy = templateCopy.replace("{atrybut_nazwa}", key[:-1])
                templateCopy = templateCopy.replace("{atrybut_wartosc}", x[key])
                return [templateCopy]

def generateQueryForFeatures(product, template) -> list:
    li = []
    for x in product["traits"]:
        for key in x.keys():
            if not (key in ["Kod EAN:", "Smak:"]):
                templateCopy = template[:]
                templateCopy = replaceBasicValues(product, templateCopy)
                templateCopy = templateCopy.replace("{nazwa_cechy}", key[:-1])
                templateCopy = templateCopy.replace("{wartosc_cechy}", x[key])
                li.append(templateCopy)
    return li

def generateQueryForSingleTable(product, template) -> list:
    templateCopy = template[:]
    templateCopy = replaceBasicValues(product, templateCopy)
    return [templateCopy]

def getSubqueries(templateCopy: str) -> list:
    li = []
    query = []
    tableName = ""
    for x in templateCopy.split("\n"):
        if x.startswith("--"):
            tableName = x.split(":")[-1]
        
        if len(x) < 1:
            li.append(("\n".join(query), tableName))
            query = []
        else:
            query.append(x)
    
    if query:
        li.append(("\n".join(query), tableName))

    return li

def removeComments(query: str) -> str:
    li=[]
    for x in query.split("\n"):
        x = x.split("--")[0]
        x = x.strip()
        li.append(x)
    return "\n".join(li)

def generateQueryForProduct(product, template) -> list:
    li = []
    templateCopy = template[:]
    subQueries = getSubqueries(templateCopy)
    for tup in subQueries:
        query = tup[0]
        query = removeComments(query)
        tableName = tup[1]
        # print(tableName)

        if tableName in ["ps_product", "ps_product_lang", "ps_product_shop", "ps_image", "ps_image_lang", "ps_image_shop", "ps_stock_available"]:
            sql = generateQueryForSingleTable(product, query)
        # smak
        elif tableName in ["ps_product_attribute", "ps_product_attribute_combination", "ps_product_attribute_shop", "ps_stock_available_attrib"]:
            sql = generateQueryForAttribs(product, query)
        # pozstałe cechy, oprócz kod EAN
        elif tableName in ["ps_feature_value_lang", "ps_feature_product", "ps_feature_value"]:
            sql = generateQueryForFeatures(product, query)
        # kategorie
        elif tableName in ["ps_category_product"]:
            sql = generateQueryForCategories(product, query)

        if sql:
            for x in sql:
                if x and len(x) > 0:
                    li.append(x)
    return li

def generateQuery(scrapData, queryTemplate) -> list:
    li = []
    li.append("SET AUTOCOMMIT=0;")
    li.append("START TRANSACTION;")
    for prod in scrapData:
        sql = generateQueryForProduct(prod, queryTemplate)

        li.append("/*" + (98* "*"))
        li.append(prod["name"])
        li.append((98* "*") + "*/")

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
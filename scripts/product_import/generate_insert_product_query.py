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
    url = url.replace("/", "-")
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
    templateCopy = templateCopy.replace("{nazwa}", product["name"])
    templateCopy = templateCopy.replace("{link}", getLink(product["name"]))
    templateCopy = templateCopy.replace("{product_type}", "3")
    templateCopy = templateCopy.replace("{opis}", product["description"])
    templateCopy = templateCopy.replace("{image_id}", str(product["image_id"]))
    return templateCopy

def generateQueryForAttribs(product, template) -> list:
    elementToRemove=[]
    for x in product["traits"]:
        for key in x.keys():
            if key != "Smak:":
                elementToRemove.append(x)
                
    for x in elementToRemove:
        product["traits"].remove(x)

    if len(product["traits"])==0:
        return

    for x in product["traits"]:
        key = list(x.keys())[0]
        templateCopy = template[:]
        templateCopy = replaceBasicValues(product, templateCopy)
        templateCopy = templateCopy.replace("{atrybut_nazwa}", key[:-1])
        templateCopy = templateCopy.replace("{atrybut_wartosc}", x[key])
        return [templateCopy]

def generateQueryForFeatures(product, template) -> list:
    elementToRemove=[]
    for x in product["traits"]:
        for key in x.keys():
            if key == "Kod EAN:":
                elementToRemove.append(x)
            elif key == "Smak:":
                elementToRemove.append(x)
                
    for x in elementToRemove:
        product["traits"].remove(x)

    if len(product["traits"]) == 0:
        return
    
    li = []
    for x in product["traits"]:
        key = list(x.keys())[0]
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
    tableName =""
    for x in templateCopy.split("\n"):
        if x.startswith("--"):
            tableName = x.split(":")[-1]
        
        if len(x) <= 1:
            li.append(("\n".join(query), tableName))
            query = []
        else:
            query.append(x)
    
    if query:
        li.append(("\n".join(query), tableName))

    return li

def generateQueryForProduct(product, template) -> list:
    li = []
    templateCopy = template[:]
    subQueries = getSubqueries(templateCopy)
    for tup in subQueries:
        query = tup[0]
        tableName = tup[1]

        if tableName in ["ps_product", "ps_product_lang", "ps_product_shop", "ps_image", "ps_image_lang", "ps_image_shop"]:
            sql = generateQueryForSingleTable(product, query)
        # smak
        elif tableName in ["ps_product_attribute", "ps_product_attribute_combination", "ps_product_attribute_shop"]:
            sql = generateQueryForAttribs(product, query)
        # pozstałe cehcy, oprócz kod EAN
        elif tableName in ["ps_feature_value_lang", "ps_feature_product", "ps_feature_value"]:
            sql = generateQueryForFeatures(product, query)

        if sql:
            for x in sql:
                if x and len(x) > 0:
                    li.append(x)
    return li

def generateQuery(scrapData, queryTemplate) -> list:
    li = []
    for prod in scrapData:
        sql = generateQueryForProduct(prod, queryTemplate)
        for x in sql:
            li.append(x)
    
        # DEBUG
        break

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
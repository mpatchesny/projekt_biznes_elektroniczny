#! python3

# Skrypt, który tworzy plik SQL do importu produktów do bazy danych

import os
import sys
import json

def replaceBasicValues(product, templateCopy) -> str:
    cena = product["price"]
    cena = cena.replace(" zł", "")
    cena = cena.replace(",", ".")
    cena = float(cena)
    cena = cena * (1-0.23)
    templateCopy = templateCopy.replace("{cena_netto}", cena)

    kategoria = product["category"][:-1]
    templateCopy = templateCopy.replace("{kategoria}", kategoria)

    ean = "" # random
    for x in product["traits"]:
        if x.get("Kod EAN:"):
            ean = x.get("Kod EAN:")
    templateCopy = templateCopy.replace("{ean}", ean)
    templateCopy = templateCopy.replace("{nazwa}", product["name"])
    templateCopy = templateCopy.replace("{opis}", product["description"])
    templateCopy = templateCopy.replace("{image_id}", product["image_id"])
    return templateCopy

def generateQueryForAttribs(product, template) -> list:
    elementToRemove=[]
    for x in product["traits"]:
        for key in x.keys:
            if key != "Smak:":
                elementToRemove.append(x)
                
    for x in elementToRemove:
        product["traits"].remove(x)

    if len(product["traits"])==0:
        return

    x = product["traits"][0]
    key = list(x.keys())
    templateCopy = template[:]
    templateCopy = replaceBasicValues(product, templateCopy)
    templateCopy = templateCopy.replace("{atrybut_nazwa}", key[:-1])
    templateCopy = templateCopy.replace("{atrybut_wartosc}", x[key])
    return list(templateCopy)

def generateQueryForFeatures(product, template) -> list:
    elementToRemove=[]
    for x in product["traits"]:
        for key in x.keys:
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
    return list(templateCopy)

def generateQueryForProduct(product, template) -> list:
    li=[]
    templateCopy= template[:]
    subtemplates = templateCopy.split(");")
    for temp in subtemplates:
        temp = temp + ");"
        tableName = temp.split("\n")[0]
        tableName = tableName.split(":")[1]

        if tableName in ["ps_product", "ps_product_lang", "ps_product_shop", "ps_image", "ps_image_lang", "ps_image_shop"]:
            sql = generateQueryForSingleTable(product, temp)
        # smak
        elif tableName in ["ps_product_attribute", "ps_product_attribute_combination", "ps_product_attribute_shop"]:
            sql = generateQueryForAttribs(product, temp)
        # pozstałe cehcy, oprócz kod EAN
        elif tableName in ["ps_feature_value_lang", "ps_feature_product", "ps_feature_value"]:
            sql = generateQueryForFeatures(product, temp)

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
    return li

def main(argv):
    with open(argv[0], "r", encoding="utf-8") as f:
        scrapData = json.loads(f.read())
        
        with open(argv[1], "r", encoding="utf-8") as f2:
            queryTemplate = f2.read()
            sql = generateQuery(scrapData, queryTemplate)

            with open("INSERT_PRODUCTS.sql", "w", encoding="utf-8") as f3:
                f3.write(sql.join("\n\n\n"))

main(sys.argv[1:])
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

def generateQueryForProduct(product, queryTemplate) -> str:
    pass

def generateQuery(scrapData, queryTemplate) -> list:
    pass

def main(argv):
    with open(argv[0], "r", encoding="utf-8") as f:
        scrapData = json.loads(f.read())
        
        with open(argv[1], "r", encoding="utf-8") as f2:
            queryTemplate = f2.read()
            sql = generateQuery(scrapData, queryTemplate)

            with open("INSERT_PRODUCTS.sql", "w", encoding="utf-8") as f3:
                f3.write(sql.join("\n\n\n"))

main(sys.argv[1:])
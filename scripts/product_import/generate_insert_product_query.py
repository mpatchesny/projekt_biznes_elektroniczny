#! python3

# Skrypt, który tworzy plik SQL, który importuje produkty do bazy danych

import os
import sys
import json

def replacePolishDiacritics(text):
    polish = "ęółśążźćń"
    latin = "eolsazzcn"
    for i in range(0, len(polish)):
        text = text.replace(polish[i], latin[i])
    return text

def main(argv):
    with open(argv[0], "r") as f:
        scrapData = json.loads(f.read())
        # TODO


main(sys.argv[1:])
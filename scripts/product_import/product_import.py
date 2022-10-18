#! python3

# Skrypt, który tworzy pliki csv gotowe do importu do sklepu Prestashop
# na podstawie wyniku ze skryptu webscraper.py

import os
import sys
import json

def main(argv):

    with open(argv[0], "r") as f:
        data = json.loads(f.read())


main(sys.argv[1:])
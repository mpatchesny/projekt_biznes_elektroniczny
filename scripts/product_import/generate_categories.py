#! python3

# Skrypt, który tworzy pliki csv z kategoriami gotowe do importu do sklepu Prestashop
# na podstawie wyniku ze skryptu webscraper.py

import os
import sys
import json

class Category:
    def __init__(self, categoryId, active, name, parentCategory, isRoot, url):
        self.categoryId = categoryId
        self.active = active
        self.name = name
        self.parentCategory = parentCategory
        self.isRoot = isRoot
        self.url = url

    def toCsvString(self, delim):
        return f'{self.categoryId}{delim}{self.active}{delim}{self.name}{delim}{self.parentCategory}{delim}{self.isRoot}{delim}{delim}{delim}{delim}{delim}{self.url}{delim}'

    def __str__(self):
        return f"{self.categoryId} {self.active} {self.name} {self.parentCategory} {self.isRoot} {self.url}"

def replacePolishDiacritics(text):
    polish = "ęółśążźćń"
    latin = "eolsazzcn"
    for i in range(0, len(polish)):
        text = text.replace(polish[i], latin[i])
    return text

def createCategories(scrapData):
    # Fields: Category ID, Active (0/1), Name *, Parent category, Root category (0/1), Description, Meta title, Meta keywords, Meta description, URL rewritten, Image URL
    currentCategoryId = 0

    allCategories = []
    for i in range(0, 10):
        for x in scrapData:
            categories = x["category"]
            if len(categories) > i:
                categoryAlreadyAdded = False
                # isRoot = int((i == 0))
                isRoot = 0
                url = str(categories[i]).lower().replace(" ", "-")
                url = replacePolishDiacritics(url)
                url = url.replace(",", "")
                url = url.replace("/", "-")
                
                for tempCat in allCategories:
                    if tempCat.name == categories[i]:
                        categoryAlreadyAdded = True

                parentCat = None
                if i > 0:
                    for tempCat in allCategories:
                        if tempCat.name == categories[i-1]:
                            parentCat = tempCat

                if not categoryAlreadyAdded:
                    currentCategoryId += 1
                    parentCategoryName = ""
                    if parentCat: 
                        parentCategoryName = parentCat.name
                    c = Category(currentCategoryId, 1, categories[i], parentCategoryName, isRoot, url)
                    allCategories.append(c)
    
    return allCategories

def main(argv):
    with open(argv[0], "r") as f:
        scrapData = json.loads(f.read())
        categories = createCategories(scrapData)

        with open("categories.csv", "w", encoding="utf-8") as f2:
            f2.write("Category ID;Active (0/1);Name *;Parent category;Root category (0/1);Description;Meta title;Meta keywords;Meta description;URL rewritten;Image URL\n")
            for c in categories:
                f2.write(c.toCsvString(";") + "\n")


main(sys.argv[1:])
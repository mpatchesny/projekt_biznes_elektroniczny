#! python3

# Skrypt, który tworzy pliki csv z produktami i kategoriami gotowe do importu do sklepu Prestashop
# na podstawie wyniku ze skryptu webscraper.py

import os
import sys
import json

class Product:
    def __init__(self, productId, name, categories, priceWithoutTax, taxId, priceFull, unity, unitPrice, summary, description, tags, url, imageUrl, features):
        pass

    def toCsvString(self):
        pass

    def __str__(self):
        pass

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

def createProducts(scrapData, categories):
    # Product ID;Active (0/1);Name *;Categories (x,y,z...);Price tax excluded;Tax rules ID;Wholesale price;On sale (0/1);Discount amount;Discount percent;Discount from (yyyy-mm-dd);Discount to (yyyy-mm-dd);Reference #;Supplier reference #;Supplier;Manufacturer;EAN13;UPC;Ecotax;Width;Height;Depth;Weight;Delivery time of in-stock products;Delivery time of out-of-stock products with allowed orders;Quantity;Minimal quantity;Low stock level;Send me an email when the quantity is under this level;Visibility;Additional shipping cost;Unity;Unit price;Summary;Description;Tags (x,y,z...);Meta title;Meta keywords;Meta description;URL rewritten;Text when in stock;Text when backorder allowed;Available for order (0 = No, 1 = Yes);Product available date;Product creation date;Show price (0 = No, 1 = Yes);Image URLs (x,y,z...);Image alt texts (x,y,z...);Delete existing images (0 = No, 1 = Yes);Feature(Name:Value:Position);Available online only (0 = No, 1 = Yes);Condition;Customizable (0 = No, 1 = Yes);Uploadable files (0 = No, 1 = Yes);Text fields (0 = No, 1 = Yes);Out of stock action;Virtual product;File URL;Number of allowed downloads;Expiration date;Number of days;ID / Name of shop;Advanced stock management;Depends On Stock;Warehouse;Acessories (x,y,z...)
    pass

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
        product = createProducts(scrapData, categories)

        with open("categories.csv", "w", encoding="utf-8") as f2:
            f2.write("Category ID;Active (0/1);Name *;Parent category;Root category (0/1);Description;Meta title;Meta keywords;Meta description;URL rewritten;Image URL\n")
            for c in categories:
                f2.write(c.toCsvString(";") + "\n")


main(sys.argv[1:])
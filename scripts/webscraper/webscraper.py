#! python3

# Skrypt do scrapowania produktow ze strony sklepu ostrovit.com

import json
import requests
import os
import sys
import bs4
import time
import random
import logging
logging.basicConfig(level = logging.INFO, format=" %(asctime)s - %(levelname)s - %(message)s")

URL_DOMAIN = "https://ostrovit.com"

def dumpResults(list, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(list, f)

def scrapProductPage(page, scrapPageCount):
    
    logging.info(f"...scraping {scrapPageCount}: {page}")

    res = requests.get(page)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    pageScrap = {}

    # Nazwa, cena
    pageScrap["url"] = page
    if soup.find(class_ = "projector__name"):
        pageScrap["name"] = soup.find(class_ = "projector__name").text
    else:
        # brak takiego produktu
        return
    pageScrap["price"] = soup.find(class_ = "projector__price").text

    # Pobieranie cech produktu
    traits = []
    for item in soup.find_all(class_ = "projector__trait"):
        d = {}
        d[item.find("strong").text] = item.find("span").text
        traits.append(d)
    pageScrap["traits"] = traits

    # Pobieranie kategorii produktu
    category = []
    for item in soup.find_all(class_ = "category"):
        if item.a:
            cat = item.a.text
        else:
            cat = item.text
        
        if category.count(cat) == 0:
            category.append(cat)
    pageScrap["category"] = category

    # Pobieranie smakow/ wariantow produktu
    if soup.find(class_ = "projector__version"):
        pageScrap["versions_name"] = soup.find(class_ = "projector__version").next_element.find("strong").text

    versions = []
    innerHtml = soup.find(class_ = "f-select-versions")
    if innerHtml:
        innerHtml = str(innerHtml)
        soup2 = bs4.BeautifulSoup(innerHtml, "html.parser")
        for item in soup2.find_all("option"):
            versions.append(item.text)
    pageScrap["versions"] = versions

    if soup.find(class_ = "cm__text --bold"):
        pageScrap["description"] = soup.find(class_ = "cm__text --bold").text

    # Pobieranie zdjecia
    for pic in soup.find_all('img'):
        if pic.get("width") == "450" and pic.get("height") == "450":
                remotePath = URL_DOMAIN + pic["src"]
                imageName = pic["src"].split("/")[-1]
                localPath = os.path.join(os.getcwd(), "images", imageName)
                pageScrap["local_path"] = localPath

                res2 = requests.get(remotePath)
                res2.raise_for_status()
                with open(localPath, 'wb') as imageFile:
                    for chunk in res2.iter_content(100000):
                        imageFile.write(chunk)
                break

    return pageScrap

def visitPage(page, RESULTS, resultsPath):
    logging.info("visiting " + page)

    if os.path.exists(page):
        with open(page, "r", encoding="utf-8") as f:
            html = f.read()
    else:
        res = requests.get(page)
        res.raise_for_status()
        html = res.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    # Szukanie i odwiedzanie odnosnikow
    visited = []
    for link in soup.find_all(class_ = "product__icon-link"):
        if len(visited) > 150:
            break

        actualLink = link.get("href", "n/a")
        if actualLink.find("products/ostrovit") > 0:
            linkToVisit = actualLink
            
            li = [x["url"] for x in RESULTS]
            if li.count(linkToVisit) == 0:
                pageScrap = scrapProductPage(linkToVisit, len(visited)+1)
                if pageScrap:
                    RESULTS.append(pageScrap)
                    dumpResults(RESULTS, resultsPath)
                    visited.append(actualLink)
                    
                    randomTime = random.randrange(5, 20)
                    logging.debug(f"...sleep {randomTime}")
                    for i in range(1, randomTime):
                        time.sleep(1)
def main(argv):

    # Tworzenie folderu gdzie trafia zdjecia produktow
    imagePath = os.path.join(os.getcwd(), "images")
    if not os.path.exists(imagePath):
        os.mkdir(imagePath)

    results = []
    resultsPath = os.path.join(os.getcwd(), "results.json")

    # Pobieranie danych visited, results
    if os.path.exists(resultsPath):
        with open(resultsPath, "r") as f:
            RESULTS = json.loads(f.read())

    # Glowna petla
    for file in argv:
        visitPage(file, RESULTS, resultsPath)

main(sys.argv[1:])
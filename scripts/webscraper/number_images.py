#! python3

# Prosty skrypt do numerowania obrazków: obrazki w prestashopie są numerowane w kolejności
# dzięki temu będzie można dodać obrazki masowo do sklepu, a następnie przypisać je
# nowym produktom

import os
import json

# Sczytywanie obrazków z folderu images w kolejności

images=[]
for _, _, files in os.walk("images"):
    for x in files:
        path = os.getcwd() + "\\images\\" + x
        images.append(path)

with open("result_no_dumps.json", "r") as f:
    results = json.loads(f.read())

startImageId = 506
for x in results:
    if x.get("local_path"):
        filename = x["local_path"]
        filename = filename.split("\\")[-1]
        localFixed = os.getcwd() + "\\images\\" + filename
        if localFixed in images:
            position = images.index(localFixed)
            x["image_id"] = startImageId + position
        else:
            print(localFixed + " nie znaleziono")
    else:
        print(x["name"] + " brak klucza local_path")

with open("result_images_numbered.json", "w", encoding="utf-8") as f:
    json.dump(results, f)
#! python3

# Prosty skrypt do numerowania obrazków: obrazki w prestashopie są numerowane w kolejności
# dzięki temu będzie można dodać obrazki masowo do sklepu, a następnie przypisać je
# nowym produktom

import os
import json
import math
import shutil

# Zapisywanie obrazków z folderu images w kolejności

with open("result_no_dumps.json", "r") as f:
    results = json.loads(f.read())

imageId = 1
filesPerFolder = 20
for x in results:
    if x.get("local_path"):
        filename = x["local_path"]
        filename = filename.split("\\")[-1]
        localPathFixed = os.getcwd() + "\\images\\" + filename
        
        if os.path.exists(localPathFixed):
            newImagePath = os.getcwd() + "\\images\\" + str(math.ceil(imageId/ filesPerFolder))
            if not os.path.exists(newImagePath):
                os.mkdir(newImagePath)
            newImageName = str(imageId) + ".jpg"
            newImagePath = newImagePath + "\\" + newImageName

            shutil.copy(localPathFixed, newImagePath)
            x["image_id"] = imageId
            x["local_path_fixed"] = newImagePath
            imageId += 1
        else:
            print(localFixed + " nie znaleziono")
    else:
        print(x["name"] + " brak klucza local_path")

with open("result_images_numbered.json", "w", encoding="utf-8") as f:
    json.dump(results, f)
#! python3

# Skrypt do usuwania duplikatów z wyników działania skryptu webscraper.py

import os
import json

with open("results.json", "r") as f:
    RESULTS = json.loads(f.read())

li=[]
match=False
for i in range(0, len(RESULTS)-1):
    for j in range(i+1, len(RESULTS)):
            if i!= j:
                if RESULTS[i]["url"]==RESULTS[j]["url"]:
                    match = True
    if not match:
        li.append(RESULTS[i])
    match = False

with open("result_no_dumps.json", "w", encoding="utf-8") as f:
    json.dump(li, f)
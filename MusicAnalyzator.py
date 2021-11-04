import json

with open("classical.json", "r", encoding="utf-8") as file:
    text = json.load(file)
    print(text)
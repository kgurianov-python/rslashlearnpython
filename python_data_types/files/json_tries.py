import json



f = open("data.json", 'r', encoding="utf-8")
js = json.load(f)
sum = sum([int(item["count"]) for item in js["comments"]])

print(sum)



import json
import re

with open('test.json', 'r', encoding='utf-8') as f:
    content = f.read()
    json_raw = re.sub('""', '"', re.sub('\\\\', '', content))
    data = json.loads(json_raw)


print(f"{data=}")
print(data['payload']['pin'])

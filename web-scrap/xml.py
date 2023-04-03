import xml.etree.ElementTree as ET


data = '''
<xml>
<comments>
<item>
  <name> "Matthias"</name>,
  <count><count>97</count></count>
</item>
<item>
  <name> "Matthias"</name>,
  <count><count>97</count></count>
</item>
</comments>
</xml>
'''


tree = ET.fromstring(data)
print(tree)
counts = tree.findall('.//item')# the type is: list
print(counts)
for item in counts:
    print(item.find('count').find('count').text)
    #the type is: <class 'xml.etree.ElementTree.Element'>
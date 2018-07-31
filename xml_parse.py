import xml.etree.cElementTree as ET
from SQL_worker import Write_to_SQL

tree = ET.parse("D\data_easy.xml")
root = tree.getroot()

#for name in .//Detail.collection.attrib.items():
#    print(name)

for data in root.findall(".//Detail"):
    a = (data.attrib["text1"])
    b = (data.attrib["text2"])
    c = (data.attrib["text3"])
    Write_to_SQL(a, b, c)


#print(root.findall(".//Detail").attrib["text2"])
#print(root.findall(".//Detail"))
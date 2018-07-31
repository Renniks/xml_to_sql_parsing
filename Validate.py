from lxml import etree

xmlschema_doc = etree.parse("D:\downloads\data\data.xsd")
xml_doc = etree.parse("D:\downloads\data\data.xml")
xmlschema = etree.XMLSchema(xmlschema_doc)

if xmlschema.validate(xml_doc):
   print('Valid xml')
else:
   print('Invalid xml')


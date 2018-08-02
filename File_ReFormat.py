import re

data = "data_bad.xml"
new_data = open('data_new.xml', 'w', encoding='utf-8')
regex = r'="((?:[^"]|"(?!\s*(?:\w+="|/>)))+)"'
i = 0
with open(data, encoding='utf-8') as file:
    for line in file.readlines():
        i += 1
        print(i)
        new_data.write(re.sub(regex, '\g<1>', line))
new_data.close()

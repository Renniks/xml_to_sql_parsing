import re

data = "data_bad.xml"
regex = "<Detail\s+Полное_и_сокращенное_наименование_организации_с_указанием_ее_организационно___правовой_формы=(.*?)\s+ИНН"
i = 0
with open(data, encoding='utf-8') as file:
    for line in file.readlines():
        i += 1
        print(i)
        print(re.sub(regex, '\g<1>', line))
        #print(re.finditer(regex, line))
        '''matches = re.finditer(regex, line, re.MULTILINE)

        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1
           print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                                end=match.end(), match=match.group()))
            print("Match found for line:", i)
            print((match.group(1)).replace('"', ""))
            for groupNum in range(1, len(match.groups())):
                groupNum = groupNum + 1
                print(match.group(groupNum))'''
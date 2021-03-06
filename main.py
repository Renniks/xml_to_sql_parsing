import xml.etree.cElementTree as ET
import sqlite3
import re

data = "data_bad.xml"
#root = tree.getroot()
regex = r'="((?:[^"]|"(?!\s*(?:\w+="|/>)))+)"'
data = re.sub(regex, "='\g<1>'", data)
print(data)
tree = ET.fromstring(data).findall('.//Detail')

"""
conn = sqlite3.connect('D:\downloads\data\Chinook_Sqlite.sqlite')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE FSRAR (
    id                                                                                                                          INTEGER PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                                                                                                                                        UNIQUE,
    Полное_и_сокращенное_наименование_организации_с_указанием_ее_организационно___правовой_формы                                TEXT,
    ИНН_организации                                                                                                             TEXT,
    КПП_организации                                                                                                             TEXT,
    Адрес__место_нахождения___организации                                                                                       TEXT,
    Адрес_электронной_почты_организации                                                                                         TEXT,
    Место_нахождения__адрес__обособленного_подразделения_организации__осуществляющего_лицензируемый_вид_деятельности            TEXT,
    КПП_обособленного_подразделения_организации__осуществляющего_лицензируемый_вид_деятельности                                 TEXT,
    Код_субъекта_Российской_Федерации_по_месту_нахождения_организации                                                           INTEGER,
    Код_субъекта_РФ_по_месту_нахождения_обособленного_подразделения_организации__осуществляющего_лицензируемый_вид_деятельности INTEGER,
    Вид_лицензируемой_деятельности_организации                                                                                  TEXT,
    Номер_ранее_выданной_лицензии                                                                                               TEXT,
    Дата_выдачи_лицензии                                                                                                        TEXT,
    Дата_окончания_действия_лицензии                                                                                            TEXT,
    Номер_лицензии__соответствующий_номеру_записи_в_реестре                                                                     TEXT,
    Сведения_о_действии_лицензии                                                                                                TEXT,
    Дата_изменения_сведений_о_действии_лицензии                                                                                 TEXT,
    Основание_изменения_сведений_о_действии_лицензии                                                                            TEXT,
    История_изменений_сведений_о_действии_лицензии                                                                              TEXT,
    Номер_бланка                                                                                                                TEXT,
    Орган_выдавший_лицензию
);''')
"""

def Write_to_SQL(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19):
    cursor.execute("INSERT INTO Test VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19))
    conn.commit()


for item in tree:
    a = (data.attrib["Полное_и_сокращенное_наименование_организации_с_указанием_ее_организационно___правовой_формы"])
    b = (data.attrib["ИНН_организации"])
    c = (data.attrib["КПП_организации"])
    d = (data.attrib["Адрес__место_нахождения___организации"])
    e = (data.attrib["Адрес_электронной_почты_организации"])
    f = (data.attrib["Место_нахождения__адрес__обособленного_подразделения_организации__осуществляющего_лицензируемый_"
                     "вид_деятельности"])
    g = (data.attrib["КПП_обособленного_подразделения_организации__осуществляющего_лицензируемый_вид_деятельности"])
    j = (data.attrib["Код_субъекта_Российской_Федерации_по_месту_нахождения_организации"])
    k = (data.attrib["Код_субъекта_РФ_по_месту_нахождения_обособленного_подразделения_организации__осуществляющего_"
                     "лицензируемый_вид_деятельности"])
    l = (data.attrib["Вид_лицензируемой_деятельности_организации"])
    m = (data.attrib["Номер_ранее_выданной_лицензии"])
    n = (data.attrib["Дата_выдачи_лицензии"])
    o = (data.attrib["Дата_окончания_действия_лицензии"])
    p = (data.attrib["Номер_лицензии__соответствующий_номеру_записи_в_реестре"])
    q = (data.attrib["Сведения_о_действии_лицензии"])
    r = (data.attrib["Дата_изменения_сведений_о_действии_лицензии"])
    s = (data.attrib["Основание_изменения_сведений_о_действии_лицензии"])
    t = (data.attrib["История_изменений_сведений_о_действии_лицензии"])
    u = (data.attrib["Номер_бланка"])
    v = (data.attrib["Орган_выдавший_лицензию"])
    print(a, b, c, d, e, f, g, j, k, l, m, n, o, p, q, r, s, t, u, v)

conn.close()

import sqlite3
conn = sqlite3.connect('Test_DB.sqlite')
cursor = conn.cursor()


def Write_to_SQL(data1, data2, data3):
    print(data1,data2,data3)
    cursor.execute("INSERT INTO Test VALUES(NULL, ?, ?, ?)", (data1, data2, data3))
    conn.commit()

#cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
#results = cursor.fetchall()
#print('SQL read =', results)


cursor.execute('''CREATE TABLE Test (
    id    INTEGER PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                  UNIQUE ON CONFLICT ROLLBACK
                 NOT NULL,
    text1 TEXT    NOT NULL,
    text2 TEXT,
    text3 TEXT);''')

import pymysql
import json
from _mysql.connection import connection, cursor

def record():
    cursor.execute("TRUNCATE status")
    cursor.execute("TRUNCATE ready")
    with open('childs.json', 'r', encoding='utf-8') as f:
        _data = json.load(f)
        for i in _data['child'].values():
            cursor.execute("INSERT INTO status (name, status) VALUES (%s, '')", i)
    connection.commit()
print(record())
import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

try:
    connection = pymysql.connect(
        host = os.getenv('HOST'),
        user= os.getenv('USER'),
        password= os.getenv('PASSWORD'),
        database= os.getenv('DATABASE')
    )
    cursor = connection.cursor()
except Exception as ex:
    print(ex)
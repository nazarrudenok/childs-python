import time
import schedule
from dotenv import load_dotenv
from _mysql.db_cheks import random_name
from _mysql.clear_status import clear_status
from _mysql.record import record
from _mysql.connection import connection

load_dotenv()

try:
    # schedule.every(15).seconds.do(clear_status)
    schedule.every().day.at('7:00').do(clear_status)
    # schedule.every(5).seconds.do(random_name)
    schedule.every().day.at('7:30').do(random_name)

    while True:
        schedule.run_pending()
        time.sleep(1)
except Exception as ex:
    record()
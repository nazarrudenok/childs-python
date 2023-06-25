import schedule
import time
from _mysql.connection import connection, cursor

def clear_status():
    cursor.execute("UPDATE status SET status = '' WHERE status = '-'")
    connection.commit()

# schedule.every(30).seconds.do(clear_status)
# schedule.every(40).seconds.do(clear_status)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

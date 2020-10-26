import time
import schedule

import kmountain1
schedule.every(3).days.do(kmountain1.mtdb)

while True:
    schedule.run_pending()
    time.sleep(1)
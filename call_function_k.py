import time
import schedule

import kstart_jerry
schedule.every(1).days.do(kstart_jerry.kdb)

while True:
    schedule.run_pending()
    time.sleep(1)
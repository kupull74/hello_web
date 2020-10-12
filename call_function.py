import test1012

test1012.sum()
test1012.print_info(name='Jerry Ko')

import time
# while True:
#     test1012.sum()
#     test1012.print_info(name="Godzilla")
#     time.sleep(5)

import schedule
# def job():
#     print("Bang Bang")
# schedule.every(30).minutes.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

import naver_movie_ko
schedule.every(30).minutes.do(naver_movie_ko.ndb)

while True:
    schedule.run_pending()
    time.sleep(1)
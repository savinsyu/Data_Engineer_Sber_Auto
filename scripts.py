import schedule
import time

def job():
    from gahits import gahits
    from gasessions import gasessions
    from dump import dump
    from delete import delete
    gahits()
    gasessions()
    dump()
    delete()

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
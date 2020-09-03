import datetime
import time


def greeting():
    return "Hi, I'm a Simple Artificial Virtual Assistant, but you can call me SAVA", True


def this_time():
    return str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S. %m/%d/%Y')), True


task = {
    "greeting": greeting(),
    "time": this_time()
}


def search(x1):
    for t in task:
        if t in x1:
            return task[t]
    return "Sorry, I can't do it", True

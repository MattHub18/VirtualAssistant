from functionality import *

task = {
    "greeting": greeting(),
    "time": this_time(),
    "speedtest": spt(),
    "joke": jk()
}


def search(x1):
    for t in task:
        if t in x1:
            return task[t]
    return "Sorry, I can't do it", True

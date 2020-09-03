def greeting():
    return "Hi, I'm a Simple Artificial Virtual Assistant, but you can call me SAVA", True


task = {
    "greeting": greeting()
}


def search(x1):
    for t in task:
        if t in x1:
            return task[t]
    return "Sorry, I can't do it", True

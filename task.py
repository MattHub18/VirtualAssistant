import datetime
import random
import time
import tkinter as tk

from speedtest import Speedtest

from music_mixer import Mixer


def search(x1):
    if "greeting" in x1:
        return "Hi, I'm a Simple Artificial Virtual Assistant, but you can call me SAVA", True

    elif "time" in x1:
        return str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S. %m/%d/%Y')), True

    elif "speedtest" in x1:
        st = Speedtest()
        st.get_servers([])
        download = str(round((st.download() / 1024) / 1024, 2))
        upload = str(round((st.upload() / 1024) / 1024, 2))
        ping = str(round(st.results.ping, 2))
        return "Ping: " + ping + " milliseconds. Download: " + download + " MB. Upload: " + upload + " MB.", True

    elif "joke" in x1:
        rd = random.randint(1, 30)
        if rd % 3 == 0:
            return "There are 1 0 types of people, who understand binaries and who don't", True
        elif rd % 3 == 1:
            return "A software developer brought his pet to work. It was a cute Python", True
        elif rd % 3 == 2:
            return "Where does programmer go on holiday? To the C", True

    elif "playlist" in x1:
        mixer = tk.Toplevel()
        app = Mixer(mixer, 'res/disc.png')
        mixer.wait_window()
        app.exit()
        return "", False
    else:
        return "Sorry, I can't do it", True

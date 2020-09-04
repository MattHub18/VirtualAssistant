import datetime
import time

from speedtest import Speedtest


def greeting():
    return "Hi, I'm a Simple Artificial Virtual Assistant, but you can call me SAVA", True


def this_time():
    return str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S. %m/%d/%Y')), True


def spt():
    st = Speedtest()
    st.get_servers([])
    download = str(round((st.download() / 1024) / 1024, 2))
    upload = str(round((st.upload() / 1024) / 1024, 2))
    ping = str(round(st.results.ping, 2))
    return "Ping: " + ping + " milliseconds. Download: " + download + " MB. Upload: " + upload + " MB.", True

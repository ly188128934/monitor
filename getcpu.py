#coding:utf-8
import time
import psutil
import urllib2

while True:
    data = psutil.cpu_times()
    dataDict = {
        "userTime":str(data.user),
        "systemTime":str(data.system),
        "waitIo":str(data.iowait),
        "idle":str(data.idle)
}
    strData = "?%s=%s&%s=%s&%s=%s&%s=%s"
    urlData = strData%("userTime",data.user,"systemTime",data.system,"waitIo",data.iowait,"idle",data.idle)
    url = "http://127.0.0.1:8000/cgi-bin/index.py"+urlData
    print urllib2.urlopen(url).read()
    time.sleep(2)

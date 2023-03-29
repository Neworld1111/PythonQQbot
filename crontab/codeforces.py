import requests
from lxml import etree
import time
import json

def get_url(url):
    # 获取页面文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
    }
    res = requests.get(url, headers=headers)
    html = res.content.decode("utf-8")
    return html

def Unix_time(dt): # Time -> Unix Time
    #转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    timestamp = int(time.mktime(timeArray))
    return timestamp

def Real_time(dt): # Unix Time -> Time
    t = time.gmtime(dt)
    return str(t.tm_year) + '-' + str(t.tm_mon).rjust(2,'0') + '-' + str(t.tm_mday).rjust(2,'0') + ' ' + str(t.tm_hour).rjust(2,'0') + ':'+str(t.tm_min).rjust(2,'0')+ ':'+str(t.tm_sec).rjust(2,'0')


def getNextCodeforces():

    # codeforces 提供了api 返回了比赛列表
    data = get_url('https://codeforces.com/api/contest.list?gym=false')
    
    data = json.loads(data) # 转成字典
    if data['status'] != 'OK' : return []
    data = data["result"]
    result = []
    for contest in data:
        if contest['phase'] != 'BEFORE' : break
        result.append( [ contest['startTimeSeconds'], contest['name'] , 'https://codeforces.com/contests/' + str(contest['id']) ] )

    if len(result) >= 1: return result[-1]
    return []

def checkCodeforces():
    contest = getNextCodeforces()
    if len(contest)!=0:
        diff = contest[0] - int(time.mktime(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '%Y-%m-%d %H:%M:%S')))
        return diff//3600 + 1
    else: return 100


# print(getNextCodeforces())
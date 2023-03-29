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

def getAtcoder():
    tree = etree.HTML( get_url('https://atcoder.jp/') )
    result = []
    for i in range(1,3):
        
        # 获取比赛名称 地址 时间
        title = tree.xpath('//*[@id="contest-table-upcoming"]/div/table/tbody/tr[{0}]/td[2]/small/a/text()'.format(i))
        link = tree.xpath('//*[@id="contest-table-upcoming"]/div/table/tbody/tr[{0}]/td[2]/small/a/@href'.format(i))
        time = tree.xpath('//*[@id="contest-table-upcoming"]/div/table/tbody/tr[{0}]/td[1]/small/a/time/text()'.format(i))
        if len(title)==0: break

        # time转Unix format时间戳
        # time = 2023-01-29 21:00:00+0900
        # 先变成UTC+8
        # 日本时间快一个小时 
        time = Unix_time(time[0][0:19]) - 1*3600 + 8*3600

        result.append( [ time , title[0] , 'https://atcoder.jp/' + link[0] ] )

    return result

def getCodeforces():

    # codeforces 提供了api 返回了比赛列表
    data = get_url('https://codeforces.com/api/contest.list?gym=false')
    data = json.loads(data)["result"] # 转成字典

    result = []
    for contest in data:
        if contest['phase'] != 'BEFORE' : break
        result.append( [ contest['startTimeSeconds']+8*3600 , contest['name'] , 'https://codeforces.com/contests/' + str(contest['id']) ] )

    if len(result) >= 2: return [result[-1],result[-2]]
    elif len(result)==1 : return [result[0]]
    return []


def getNowcoder():
    # 直接抄抄Atcoder的就好了
    tree = etree.HTML( get_url('https://ac.nowcoder.com/acm/contest/vip-index') )
    result = []
    for i in range(2,4):
        
        # 获取比赛名称 地址 时间
        title = tree.xpath('/html/body/div/div[3]/div[1]/div[2]/div[{0}]/div[2]/div[1]/h4/a/text()'.format(i))
        link  = tree.xpath('/html/body/div/div[3]/div[1]/div[2]/div[{0}]/div[2]/div[1]/h4/a/@href'.format(i))
        time  = tree.xpath('/html/body/div/div[3]/div[1]/div[2]/div[{0}]/div[2]/div[1]/ul/li[2]/text()'.format(i))
        if len(title)==0: break

        # '比赛时间：    2023-01-30 13:00\n 至     2023-01-30 18:00\n (时长:5小时)'
        # UTC + 8
        time = Unix_time(time[0][9:25]+":00") + 8*3600
        result.append(  [ time , title[0] , 'https://ac.nowcoder.com/' + link[0] ] )

    return result

def getContest():

    resultNowcoder = getNowcoder()
    resultAtcoder = getAtcoder()
    resultCodeforces = getCodeforces()

    sstr = 'Hello~ 我是CE酱捏\n'
    
    sstr += '近期牛客比赛：\n'
    if(len(resultNowcoder)==0): sstr += 'None\n\n'
    else:
        for contest in resultNowcoder:
            sstr += contest[1] + '\n' + contest[2] + '\n' + Real_time(contest[0]) + '\n\n'

    sstr += '\n'

    sstr += '近期Codeforces比赛：\n'
    if(len(resultCodeforces)==0): sstr += 'None\n\n'
    else:
        for contest in resultCodeforces:
            sstr += contest[1] + '\n' + contest[2] + '\n' + Real_time(contest[0]) + '\n\n'

    sstr += '\n'

    sstr += '近期Atcoder比赛：\n'
    if(len(resultAtcoder)==0): sstr += 'None\n\n'
    else:
        for contest in resultAtcoder:
            sstr += contest[1] + '\n' + contest[2] + '\n' + Real_time(contest[0]) + '\n\n'
    
    return sstr
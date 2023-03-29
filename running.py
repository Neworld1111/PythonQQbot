group_id = 433934253

import time
from crontab import Send
# 设置定时器，定时执行发送消息的函数


from crontab import GoodMorning # 早安
from crontab import oj # 各大OJ比赛提醒
from crontab import codeforces
from crontab import bilibili

contest_one_day = 0
last_bilibili = 0

while True:

    now = time.strftime('%H:%M', time.localtime())
    if now == '00:00': 
        contest_one_day = 0
        last_bilibili = 0

    # -------------定时任务-------------------
    if now == '08:00': Send.SendtoGroup( group_id ,GoodMorning.Hello() ) # 向指定群号发送信息
    if now == '12:00': Send.SendtoGroup( group_id ,'每日自动提醒！\n\n'+oj.getContest())
    
    # -------------计时任务-------------------

    if contest_one_day==0 and codeforces.checkCodeforces()==1:
        contest_one_day = 1
        data = codeforces.getNextCodeforces()
        msg = data[1] + '\n' + data[2] + '\n还有不到一小时捏~来速速上分'
        Send.SendtoGroup( group_id , msg )

    if last_bilibili==0 and bilibili.get_live_status(498088093)==1:
        last_bilibili = 1
        msg = '快来围观捏!B站用户498088093开始直播啦\nhttps://live.bilibili.com/22476234'
        Send.SendtoGroup( group_id , msg )
    

    time.sleep(60)

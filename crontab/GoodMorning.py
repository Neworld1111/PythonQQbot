import time

Todo_Table = [ 
    ['2023华师大校赛rated','2023-04-1 13:00:00'] ,
    ['2023蓝桥杯省赛','2023-04-8 13:00:00'] ,   
    ['2023天梯赛rated','2023-04-22 13:00:00']
]


def Hello():

    Year = time.strftime('%Y', time.localtime())
    Month = time.strftime('%m', time.localtime())
    Day = time.strftime('%d', time.localtime())
    Week = time.strftime('%w', time.localtime())

    msg = '早上好捏! 今天是{}-{}-{}\n'.format(Year,Month,Day)
    if Week=='1': msg += '星期一：今天麦当劳O麦金会员可以领券'
    elif Week=='2': msg += '星期二：没事的话希望来431捏'
    elif Week=='3': msg += '星期三：这周已经三天了 你打题了吗'
    elif Week=='4': msg += '星期四：今天我想吃KFC捏'
    elif Week=='5': msg += '星期五：明天要训练了捏'
    elif Week=='6': msg += '星期六：今天你来431了吗'
    elif Week=='7': msg += '星期天：明天要上课哦'
    msg += '\n\n'
    for contest in Todo_Table:
        time1 = time.strptime(contest[1], '%Y-%m-%d %H:%M:%S')
        time2 = time.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '%Y-%m-%d %H:%M:%S')
        diff_time = time.mktime(time1) - time.mktime(time2)
        struct_time = time.gmtime(diff_time)
        msg += '距离{0}还有{1}天\n'.format(contest[0],struct_time.tm_mday-1)
    return msg


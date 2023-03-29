import requests
import json

def SendtoGroup( group_id , message , call = 0 ):
    
    # 向本地5700端口发送get请求
    # id: int64
    # message: string
    # call：int64 (call = -1 时at全体成员)
    
    if (call == -1) : 
        response = requests.get('http://127.0.0.1:5700/get_group_at_all_remain?group_id={}'.format(group_id))
        # print(response.json())
        if response.json()['data']['can_at_all']: message = '[CQ:at,qq=all]' + message
        else : message = '@全体成员(今天次数不够了捏) ' + message
    elif call != 0: message = '[CQ:at,qq={}]'.format(call) + message

    return requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id=%s&message=%s' % (group_id,message))

def SendtoUser( user_id , message ):
    return requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id=%s&message=%s' % (user_id,message))
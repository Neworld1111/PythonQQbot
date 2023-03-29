# -*- coding: UTF-8 -*-
from flask import Flask, request
from crontab import oj, Send

group_id = 433934253

app = Flask(__name__)
@app.route('/',methods=['POST'])
def post_data():
    if request.get_json().get('message_type')=='group':# 如果是群聊信息
    
        gid = request.get_json().get('group_id') # 获取群号
        uid = request.get_json().get('sender').get('user_id') # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message') # 获取原始信息
        
        # 操作群消息
        print(gid,uid,message)

        if message=='contest':
            Send.SendtoGroup( group_id , oj.getContest())

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5701)

import requests
import json


def get_live_status(mid):
    url = f'https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld?mid={mid}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url=url, headers=headers)
    data = json.loads(response.text)

    if data['code'] == 0:
        return data['data']['liveStatus']
    else:
        return -1

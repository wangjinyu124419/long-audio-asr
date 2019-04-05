# -*- coding: utf-8 -*-
import os
import time

import urllib.parse
import urllib.request
import hashlib
import base64
import uuid
import wave

import requests
import urllib
import json


app_id = 'xxx',
app_key='xxx'
url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_wxasrlong'

#我们自己的阿里云服务器的地址开了8322端口,来跑我的tornado服务
callback_url='https:/xxxx：8322'
# callback_url='http://localhost:8322'


def md5(string):
    md = hashlib.md5()
    md.update(string.encode('utf-8'))
    md5 = md.hexdigest().upper()
    return md5


def urlencode(args):
    tuples = [(k, args[k]) for k in sorted(args.keys()) if args[k]]
    query_str = urllib.parse.urlencode(tuples)
    return query_str


def signify(args, app_key):
    query_str = urlencode(args)
    query_str = query_str + '&app_key=' + app_key
    signiture = md5(query_str)
    return signiture


def http_post(api_url, args):
    resp = requests.post(url=api_url, data=args)
    resp = json.loads(resp.text)
    return resp

def get_wav_time(file_path):
    #获取时间用第三方库pydub更方便,生成实例AudioSegment实例，调用duration_seconds属性,不过懒得改了
    wave_f = wave.open(file_path, 'r')
    nframe = wave_f.getnframes()
    frame_rate=wave_f.getframerate()
    wav_time=nframe//frame_rate
    return wav_time

def send_file(file_path):
    f = open(file_path, 'rb')
    file_content = f.read()

    base64_audio = base64.b64encode(file_content)
    uuidstr = uuid.uuid4().hex

    body = {
        'app_id': '2113196713',
        'format': '1',
        'callback_url': 'http://47.105.69.153:8322',
        'speech': base64_audio,
        'time_stamp': str(time.time()),
        'nonce_str': uuidstr,
        'sign': ''
    }

    body['sign'] = signify(body, 'HoMecLBIe6xvJpLC')

    resp = http_post(url, body)
    f.close()
    return resp







def get_result(file_path):
    index=0

    resp=send_file(file_path)
    if resp.get('ret')!=0:
        print('上传音频失败')
        print('resp',resp)
        return
    task_id = resp['data']['task_id']
    print(task_id)

    wav_time=get_wav_time(file_path)
    print('wav_time:',wav_time)

    while True:
        print(index)
        #尝试五次,失败就跳出循环
        if index>5:
            return ''

        res = requests.get(url='http://xxxx:8323')
        res_dict = res.json()

        try:
            text = res_dict[task_id]
        except Exception as e:
            index+=1
            print('----------',e)
        else:
            return text

                # return text
        time.sleep(wav_time // 3)




if __name__ == '__main__':
    files_path='/home/wangjinyu/workproject/long_audio_asr/res/middle_wav'
    # files_path='/home/wangjinyu/workproject/long_audio_asr/res/one_minute'
    files_list=os.listdir(files_path)
    for file in files_list:
        if files_list.index(file) >10:
            break
        file_path=os.path.join(files_path,file)
        print(file_path)
        # #
        # trecv = threading.Thread(target=get_result(file_path))
        # trecv.start()

        res=get_result(file_path)
        # print("识别结果：",res)


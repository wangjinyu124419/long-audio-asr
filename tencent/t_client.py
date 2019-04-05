# -*- coding: utf-8 -*-
import logging
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
import threading

from tencent.callback_url import setup_logging

setup_logging(filename='client_server.log',stream=False)

#屏蔽urllib3日志
logging.getLogger('urllib3').setLevel(logging.WARNING)
logger=logging.getLogger('client')

# app_id = '2113196713',
# app_key='HoMecLBIe6xvJpLC'
url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_wxasrlong'
callback_url='http://47.105.69.153:8322'
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
    # body['speech'] = base64_audio
    # body['nonce_str'] = uuidstr
    # body['time_stamp'] = str(time.time())
    # print('body',body)
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
        logger.debug('上传音频失败:%r'%resp)
        return
    task_id = resp['data']['task_id']
    logger.debug('task_id:%r'%task_id)

    wav_time=get_wav_time(file_path)
    logger.debug('wav_time:%r'%wav_time)

    # while True:
    #     print(index)
    #     if index>5:
    #         return ''
    #
    #     res = requests.get(url='http://47.105.69.153:8323')
    #     res_dict = res.json()
    #
    #     try:
    #         text = res_dict[task_id]
    #     except Exception as e:
    #         index+=1
    #         print('----------',e)
    #     else:
    #         return text
    #
    #             # return text
    #     time.sleep(wav_time // 3)




if __name__ == '__main__':
    files_path='/home/wangjinyu/workproject/long_audio_asr/res/middle_wav'
    # files_path='/home/wangjinyu/workproject/long_audio_asr/res/one_minute'
    # file_path='/home/wangjinyu/workproject/long_audio_asr/res/middle_wav/wav_25s_29.wav'
    # res=get_result(file_path)

    files_list=os.listdir(files_path)
    for file in files_list:
        if files_list.index(file)>9:
            break
        # if files_list.index(file) <=9 or files_list.index(file)>=20:
        #     continue
        file_path=os.path.join(files_path,file)
        logger.debug('音频路径:%r'%file_path)



        # #
        # trecv = threading.Thread(target=get_result(file_path))
        # trecv.start()
    #
        res=get_result(file_path)
        print("识别结果：",res)
        time.sleep(120)

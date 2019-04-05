#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2018-Present Shanghai Yitu Technology Co., Ltd.
# Licensed under the Apache License, Version 2.0

from yitu_speech.clients.long_audio_client import LongAudioClient
from yitu_speech.common.utils import audio_utils

# Your app id and api key
app_id = 1518 # Your app id
api_key = 'a1cbbd73c04b40bda1498c82a2dbb497' # Your api key
slice0 = "/home/wangjinyu/workproject/long_audio_asr/res/middle_wav/wav_25s_0.wav"
slice0 = "/home/wangjinyu/workproject/long_audio_asr/res/real_wav/wav/ningjing/宁静9.wav"
# slice0 = "/home/wangjinyu/workproject/long_audio_asr/res/pcm/0.pcm"

def get_result(slice0):
    # Initialize client
    client = LongAudioClient(app_id, api_key)

    print(" create an audio")
    #calc file MD5
    # slice0 = "sample_1.wav"
    md5 = audio_utils.md5sum(slice0)

    # To create an audio
    res = client.create_audio('pcm', 1, md5)
    if res["rtn"] is None or res["rtn"] != 0 or res["audioId"] == "":
        print('create_audio fail res: %r'%res["rtn"])
        return
    audioId = res["audioId"]
    print("audio id:", audioId)

    #To upload file part
    print(" upload a slice of an audio")
    res = client.upload_slice(audioId, slice0, 0, md5)
    if res["rtn"] != 0:
        print('upload_slice fail res:%r'% res)
        return

    #post a job
    print(" post a job")
    res = client.post_job(audioId)
    if res["rtn"] != 0 or res["jobId"] == "":
        print('post_job fail res:%r'%res)
        return
    jobId = res["jobId"]
    print("job id:", jobId)

    #get a job result
    print("try to get the result")
    res = client.wait_job_complete(jobId, 10)
    # print (res["resultText"])
    return res["resultText"]


if __name__ == '__main__':


    res=get_result(slice0)
    print(res)


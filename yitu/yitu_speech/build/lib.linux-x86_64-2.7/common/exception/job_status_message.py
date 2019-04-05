
# Copyright 2018-Present Shanghai Yitu Technology Co., Ltd.
# Licensed under the Apache License, Version 2.0

_dict = {
    0: 'job initialized',
    1: 'uploading the file',
    2: 'start to recoginse speech',
    3: 'ASR completed',
    4: 'ASR failed',
    5: 'not job found'
}

def get_job_status_message(code):
    return _dict.get(code)


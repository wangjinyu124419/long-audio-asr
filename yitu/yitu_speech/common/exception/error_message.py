# Copyright 2018-Present Shanghai Yitu Technology Co., Ltd.
# Licensed under the Apache License, Version 2.0

_dict = {
    0:'success',
    100: 'internal error',
    101: 'invalid parameter',
    102: 'permission denied',
    103: 'quota limit is reached',
    104: 'fail to decode audio',
    105: 'too long audio',
    106: 'too many requests',
    107: 'duplicated name',
    108: 'server is busy',
    109: 'too large file',
    110: 'file part missed',
    111: 'Merge file failed.',
    112: 'The audio chunk should be greater than 100k',
    113: 'The total count of audio chunk should be less than 5000',
    114: 'audio id is not found',
    115: 'reach max customwords',
    116: 'customwords is not found',
    117: 'wrong format of hotword',
    118: 'File checksum does not match'
}

def get_msg(code):
    return _dict.get(code)

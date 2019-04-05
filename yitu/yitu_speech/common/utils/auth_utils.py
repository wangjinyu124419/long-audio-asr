
# Copyright 2018-Present Shanghai Yitu Technology Co., Ltd. 
# Licensed under the Apache License, Version 2.0

import hashlib
import hmac
import time


# Calculates hmac sha 256
def cal_hmac_sha256(secret_key, ori_string):
    return hmac.new(secret_key.encode('utf-8'), ori_string.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()


# Generates authentication headers
def get_auth_headers(app_id, api_key):
    time_ts = int(time.time())
    sign = cal_hmac_sha256(api_key, str(app_id) + str(time_ts))
    headers = {'x-dev-id': str(app_id), 'x-request-send-timestamp': str(time_ts), 'x-signature': sign}
    return headers

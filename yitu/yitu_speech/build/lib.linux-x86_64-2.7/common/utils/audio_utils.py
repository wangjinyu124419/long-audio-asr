
# Copyright 2018-Present Shanghai Yitu Technology Co., Ltd. 
# Licensed under the Apache License, Version 2.0

import base64
import os
import hashlib


# Converts file into base64 encoded string
def load_file_base64(file_path):
    if not os.path.isfile(file_path):
        return None

    with open(file_path, "rb") as audio_file:
        encoded_string = base64.b64encode(audio_file.read())
        return encoded_string.decode('utf-8')


def md5sum(filename):
    fd = open(filename, "r")
    fcont = fd.read()
    fd.close()
    return hashlib.md5(fcont).hexdigest()

# Copyright 2018-Present Shanghai Yitu Technology Co., Ltd. 
# Licensed under the Apache License, Version 2.0

from .error_message import get_msg


class ClientException(Exception):
    def __init__(self, code):
        Exception.__init__(self)
        self.error_code = code
        self.message = get_msg(code)

    def __str__(self):
        return "Error %s: %s" % (
            self.error_code,
            self.message,
        )

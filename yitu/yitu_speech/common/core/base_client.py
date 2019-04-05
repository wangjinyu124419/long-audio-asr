#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018-Present Shanghai Yitu Technology Co., Ltd. 
# Licensed under the Apache License, Version 2.0


import requests

from yitu.yitu_speech.common import constants
from yitu.yitu_speech.common.exception import error_code, exceptions
from yitu.yitu_speech.common.utils.auth_utils import get_auth_headers
from urllib3 import encode_multipart_formdata


# Represents the speech client instance
class BaseClient(object):
    # Constructs the instance
    def __init__(self, app_id, api_key):
        self._app_id = app_id
        self._api_key = api_key.strip()
        self._version = constants.CONSTANT_VERSION
        self._timeout = constants.CONSTANT_REQUEST_TIMEOUT

    # Returns the version
    def get_version(self):
        return self._version

    # Sets time out in second
    def set_request_timeout(self, timeout=constants.CONSTANT_REQUEST_TIMEOUT):
        self._timeout = timeout

    # Sends post request
    def _post_request(self, url, data):
        try:
            # Get the headers
            auth_headers = get_auth_headers(self._app_id, self._api_key)

            # Post
            response = requests.post(url, json=data, headers=auth_headers, timeout=self._timeout)
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
            # Raise exception
            raise exceptions.ClientException(error_code.SAAS_TIME_OUT)

        # Return
        return response.json() or {}

    # Sends put request
    def _put_multipart_request(self, url, data):
        try:
            # Get the headers
            auth_headers = get_auth_headers(self._app_id, self._api_key)

            encode_data = encode_multipart_formdata(data)
            data = encode_data[0]
            auth_headers['Content-Type'] = encode_data[1]

            # put
            response = requests.put(url, data=data, headers=auth_headers, timeout=self._timeout)
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
            # Raise exception
            raise exceptions.ClientException(error_code.SAAS_TIME_OUT)

        # Return
        return response.json() or {}

#   Sends put request
    def _get_request(self, url, data):
        try:
            # Get the headers
            auth_headers = get_auth_headers(self._app_id, self._api_key)

            # get
            response = requests.get(url, data=data, headers=auth_headers, timeout=self._timeout)
            print (response)
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
            # Raise exception
            raise exceptions.ClientException(error_code.SAAS_TIME_OUT)

        # Return
        return response.json() or {}

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018-Present Shanghai Yitu Technology Co., Ltd.
# Licensed under the Apache License, Version 2.0


from ..common import constants
from ..common.core.base_client import BaseClient
from ..common.exception import error_code
from ..common.exception.exceptions import ClientException
import os
import time


class LongAudioClient(BaseClient):
    # _asr_url = "http://long-asr-prod.yitutech.com/lasr-api/"
    _asr_url = "http://long-asr-prod.yitutech.com/lasr-api/v2/asr"

    def _post(self, url, data):
        return super(LongAudioClient, self)._post_request(url, data)

    def _put(self, url, data):
        return super(LongAudioClient, self)._put_multipart_request(url, data)

    def _get(self, url, data=None):
        return super(LongAudioClient, self)._get_request(url, data)

#    To declare an audio
    def create_audio(self, aue, num_of_parts, md5):
        audio_url = self._asr_url +"/audio"

        # Assert param
        if aue not in constants.CONSTANT_AUE_SET:
            raise ClientException(error_code.APP_RES_INVALID_PARAM)

        if num_of_parts <= 0:
            raise ClientException(error_code.APP_RES_INVALID_PARAM)

        if md5 is None or md5.strip() == "":
            raise ClientException(error_code.APP_RES_INVALID_PARAM)

        # Construct request body
        request_body = {'aue': aue, 'numOfParts': num_of_parts, "md5": md5}

        # Send request and return
        return self._post(audio_url, request_body)

#   To upload a part of an audio file
    def upload_slice(self, audio_id, filepath, slice_index, md5):
        # Assert param
        if audio_id is None or audio_id.strip() == "":
            raise ClientException(error_code.APP_RES_INVALID_PARAM)

        if not os.path.isfile(filepath) or not os.path.exists(filepath):
            raise ClientException(error_code.APP_RES_INVALID_PARAM)

        if slice_index < 0:
            raise ClientException(error_code.APP_RES_INVALID_PARAM)

        audio_url = self._asr_url + "/audio/" + str(audio_id) + "/part/" + str(slice_index)

        data = {}
        fd = open(filepath, 'rb')
        data['audioData'] = (filepath, fd.read())
        data['md5'] = md5

        # Send request and return
        return self._put(audio_url, data)

#   To post a job
    def post_job(self, audio_id, lang=1, scene=0, custom_words=(), custom_words_id=()):
        audio_url = self._asr_url + "/job"

        # Assert param
        if audio_id is None or audio_id.strip() == "":
            raise ClientException(error_code.APP_RES_INVALID_PARAM)

        if lang != constants.CONSTANT_LANG_MANDARIN or scene != constants.CONSTANT_SCENE_GENERAL:
            raise ClientException(error_code.APP_RES_INVALID_PARAM)

        request_body = {"audioId": audio_id, "lang": str(lang), "scene": scene,
                         "customWords": custom_words, "useCustomWordsID": custom_words_id}

        # Send request and return
        return self._post(audio_url, request_body)

#   To get ASR result
    def get_job_result(self, job_id):
        # Assert param
        if job_id is None or job_id.strip() == "":
            raise ClientException(error_code.APP_RES_INVALID_PARAM)

        audio_url = self._asr_url + "/job/" + job_id + "/plain"

        # Send request and return
        return self._get(audio_url)

#   try {retry} attampts to get the request
    def wait_job_complete(self, job_id, retry):
        # Assert param
        if job_id is None or job_id.strip() == "":
            raise ClientException(error_code.APP_RES_INVALID_PARAM)

        if retry < 1:
            raise ClientException(error_code.APP_RES_INVALID_PARAM)

        while retry >= 0:
            rtn = self.get_job_result(job_id)

            if rtn['jobStatus'] is None or rtn['jobStatus'] <= 2:
                time.sleep(2)
                retry = retry - 1
            else:
                return rtn

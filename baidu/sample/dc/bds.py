# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_bds', [dirname(__file__)])
        except ImportError:
            import _bds
            return _bds
        if fp is not None:
            try:
                _mod = imp.load_module('_bds', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _bds = swig_import_helper()
    del swig_import_helper
else:
    import _bds
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class BDSpeechSDK(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BDSpeechSDK, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BDSpeechSDK, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_getmethods__["get_instance"] = lambda x: _bds.BDSpeechSDK_get_instance
    if _newclass:
        get_instance = staticmethod(_bds.BDSpeechSDK_get_instance)

    def set_event_listener(self, listener, userParam):
        return _bds.BDSpeechSDK_set_event_listener(self, listener, userParam)
    __swig_getmethods__["release_instance"] = lambda x: _bds.BDSpeechSDK_release_instance
    if _newclass:
        release_instance = staticmethod(_bds.BDSpeechSDK_release_instance)

    def post(self, message, outErrorDescription):
        return _bds.BDSpeechSDK_post(self, message, outErrorDescription)
    __swig_getmethods__["do_cleanup"] = lambda x: _bds.BDSpeechSDK_do_cleanup
    if _newclass:
        do_cleanup = staticmethod(_bds.BDSpeechSDK_do_cleanup)
    __swig_getmethods__["open_log_file"] = lambda x: _bds.BDSpeechSDK_open_log_file
    if _newclass:
        open_log_file = staticmethod(_bds.BDSpeechSDK_open_log_file)
    __swig_getmethods__["close_log_file"] = lambda x: _bds.BDSpeechSDK_close_log_file
    if _newclass:
        close_log_file = staticmethod(_bds.BDSpeechSDK_close_log_file)
    __swig_getmethods__["get_sdk_version"] = lambda x: _bds.BDSpeechSDK_get_sdk_version
    if _newclass:
        get_sdk_version = staticmethod(_bds.BDSpeechSDK_get_sdk_version)
    __swig_getmethods__["set_global_param"] = lambda x: _bds.BDSpeechSDK_set_global_param
    if _newclass:
        set_global_param = staticmethod(_bds.BDSpeechSDK_set_global_param)
BDSpeechSDK_swigregister = _bds.BDSpeechSDK_swigregister
BDSpeechSDK_swigregister(BDSpeechSDK)

def BDSpeechSDK_get_instance(SDKType, outErrorDescription):
    return _bds.BDSpeechSDK_get_instance(SDKType, outErrorDescription)
BDSpeechSDK_get_instance = _bds.BDSpeechSDK_get_instance

def BDSpeechSDK_release_instance(instance):
    return _bds.BDSpeechSDK_release_instance(instance)
BDSpeechSDK_release_instance = _bds.BDSpeechSDK_release_instance

def BDSpeechSDK_do_cleanup():
    return _bds.BDSpeechSDK_do_cleanup()
BDSpeechSDK_do_cleanup = _bds.BDSpeechSDK_do_cleanup

def BDSpeechSDK_open_log_file(logFileName, fileSize=0):
    return _bds.BDSpeechSDK_open_log_file(logFileName, fileSize)
BDSpeechSDK_open_log_file = _bds.BDSpeechSDK_open_log_file

def BDSpeechSDK_close_log_file():
    return _bds.BDSpeechSDK_close_log_file()
BDSpeechSDK_close_log_file = _bds.BDSpeechSDK_close_log_file

def BDSpeechSDK_get_sdk_version():
    return _bds.BDSpeechSDK_get_sdk_version()
BDSpeechSDK_get_sdk_version = _bds.BDSpeechSDK_get_sdk_version

def BDSpeechSDK_set_global_param(param_type, value, outErrorDescription):
    return _bds.BDSpeechSDK_set_global_param(param_type, value, outErrorDescription)
BDSpeechSDK_set_global_param = _bds.BDSpeechSDK_set_global_param

class BDSSDKMessage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BDSSDKMessage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BDSSDKMessage, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _bds.new_BDSSDKMessage(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_setmethods__["name"] = _bds.BDSSDKMessage_name_set
    __swig_getmethods__["name"] = _bds.BDSSDKMessage_name_get
    if _newclass:
        name = _swig_property(_bds.BDSSDKMessage_name_get, _bds.BDSSDKMessage_name_set)
    __swig_destroy__ = _bds.delete_BDSSDKMessage
    __del__ = lambda self: None

    def set_parameter(self, *args):
        return _bds.BDSSDKMessage_set_parameter(self, *args)

    def string_param_keys(self):
        return _bds.BDSSDKMessage_string_param_keys(self)

    def int_param_keys(self):
        return _bds.BDSSDKMessage_int_param_keys(self)

    def float_param_keys(self):
        return _bds.BDSSDKMessage_float_param_keys(self)

    def char_param_keys(self):
        return _bds.BDSSDKMessage_char_param_keys(self)

    def vector_param_keys(self):
        return _bds.BDSSDKMessage_vector_param_keys(self)

    def get_parameter(self, *args):
        return _bds.BDSSDKMessage_get_parameter(self, *args)
BDSSDKMessage_swigregister = _bds.BDSSDKMessage_swigregister
BDSSDKMessage_swigregister(BDSSDKMessage)
cvar = _bds.cvar
DATA_CHUNK = cvar.DATA_CHUNK


_bds.EVoiceRecognitionRecordSampleRateAuto_swigconstant(_bds)
EVoiceRecognitionRecordSampleRateAuto = _bds.EVoiceRecognitionRecordSampleRateAuto

_bds.EVoiceRecognitionRecordSampleRate8K_swigconstant(_bds)
EVoiceRecognitionRecordSampleRate8K = _bds.EVoiceRecognitionRecordSampleRate8K

_bds.EVoiceRecognitionRecordSampleRate16K_swigconstant(_bds)
EVoiceRecognitionRecordSampleRate16K = _bds.EVoiceRecognitionRecordSampleRate16K

_bds.EVoiceRecognitionPropertyMusic_swigconstant(_bds)
EVoiceRecognitionPropertyMusic = _bds.EVoiceRecognitionPropertyMusic

_bds.EVoiceRecognitionPropertyVideo_swigconstant(_bds)
EVoiceRecognitionPropertyVideo = _bds.EVoiceRecognitionPropertyVideo

_bds.EVoiceRecognitionPropertyApp_swigconstant(_bds)
EVoiceRecognitionPropertyApp = _bds.EVoiceRecognitionPropertyApp

_bds.EVoiceRecognitionPropertyWeb_swigconstant(_bds)
EVoiceRecognitionPropertyWeb = _bds.EVoiceRecognitionPropertyWeb

_bds.EVoiceRecognitionPropertySearch_swigconstant(_bds)
EVoiceRecognitionPropertySearch = _bds.EVoiceRecognitionPropertySearch

_bds.EVoiceRecognitionPropertyEShopping_swigconstant(_bds)
EVoiceRecognitionPropertyEShopping = _bds.EVoiceRecognitionPropertyEShopping

_bds.EVoiceRecognitionPropertyHealth_swigconstant(_bds)
EVoiceRecognitionPropertyHealth = _bds.EVoiceRecognitionPropertyHealth

_bds.EVoiceRecognitionPropertyCall_swigconstant(_bds)
EVoiceRecognitionPropertyCall = _bds.EVoiceRecognitionPropertyCall

_bds.EVoiceRecognitionPropertySong_swigconstant(_bds)
EVoiceRecognitionPropertySong = _bds.EVoiceRecognitionPropertySong

_bds.EVoiceRecognitionPropertyShake_swigconstant(_bds)
EVoiceRecognitionPropertyShake = _bds.EVoiceRecognitionPropertyShake

_bds.EVoiceRecognitionPropertyMedicalCare_swigconstant(_bds)
EVoiceRecognitionPropertyMedicalCare = _bds.EVoiceRecognitionPropertyMedicalCare

_bds.EVoiceRecognitionPropertyCar_swigconstant(_bds)
EVoiceRecognitionPropertyCar = _bds.EVoiceRecognitionPropertyCar

_bds.EVoiceRecognitionPropertyCatering_swigconstant(_bds)
EVoiceRecognitionPropertyCatering = _bds.EVoiceRecognitionPropertyCatering

_bds.EVoiceRecognitionPropertyFinanceAndEconomics_swigconstant(_bds)
EVoiceRecognitionPropertyFinanceAndEconomics = _bds.EVoiceRecognitionPropertyFinanceAndEconomics

_bds.EVoiceRecognitionPropertyGame_swigconstant(_bds)
EVoiceRecognitionPropertyGame = _bds.EVoiceRecognitionPropertyGame

_bds.EVoiceRecognitionPropertyCookbook_swigconstant(_bds)
EVoiceRecognitionPropertyCookbook = _bds.EVoiceRecognitionPropertyCookbook

_bds.EVoiceRecognitionPropertyAssistant_swigconstant(_bds)
EVoiceRecognitionPropertyAssistant = _bds.EVoiceRecognitionPropertyAssistant

_bds.EVoiceRecognitionPropertyRecharge_swigconstant(_bds)
EVoiceRecognitionPropertyRecharge = _bds.EVoiceRecognitionPropertyRecharge

_bds.EVoiceRecognitionPropertyMap_swigconstant(_bds)
EVoiceRecognitionPropertyMap = _bds.EVoiceRecognitionPropertyMap

_bds.EVoiceRecognitionPropertyInput_swigconstant(_bds)
EVoiceRecognitionPropertyInput = _bds.EVoiceRecognitionPropertyInput

_bds.EVoiceRecognitionPropertyContacts_swigconstant(_bds)
EVoiceRecognitionPropertyContacts = _bds.EVoiceRecognitionPropertyContacts

_bds.EVoiceRecognitionPropertySetting_swigconstant(_bds)
EVoiceRecognitionPropertySetting = _bds.EVoiceRecognitionPropertySetting

_bds.EVoiceRecognitionPropertyTVInstruction_swigconstant(_bds)
EVoiceRecognitionPropertyTVInstruction = _bds.EVoiceRecognitionPropertyTVInstruction

_bds.EVoiceRecognitionPropertyPlayerInstruction_swigconstant(_bds)
EVoiceRecognitionPropertyPlayerInstruction = _bds.EVoiceRecognitionPropertyPlayerInstruction

_bds.EVoiceRecognitionPropertyRadio_swigconstant(_bds)
EVoiceRecognitionPropertyRadio = _bds.EVoiceRecognitionPropertyRadio

_bds.EVoiceRecognitionLanguageChinese_swigconstant(_bds)
EVoiceRecognitionLanguageChinese = _bds.EVoiceRecognitionLanguageChinese

_bds.EVoiceRecognitionLanguageCantonese_swigconstant(_bds)
EVoiceRecognitionLanguageCantonese = _bds.EVoiceRecognitionLanguageCantonese

_bds.EVoiceRecognitionLanguageEnglish_swigconstant(_bds)
EVoiceRecognitionLanguageEnglish = _bds.EVoiceRecognitionLanguageEnglish

_bds.EVoiceRecognitionLanguageSichuanDialect_swigconstant(_bds)
EVoiceRecognitionLanguageSichuanDialect = _bds.EVoiceRecognitionLanguageSichuanDialect

_bds.EPROTOCOL_DEFAULT_swigconstant(_bds)
EPROTOCOL_DEFAULT = _bds.EPROTOCOL_DEFAULT

_bds.EPROTOCOL_SEARCH_NBEST_swigconstant(_bds)
EPROTOCOL_SEARCH_NBEST = _bds.EPROTOCOL_SEARCH_NBEST

_bds.EPROTOCOL_INPUT_NBEST_PROTOCOL_swigconstant(_bds)
EPROTOCOL_INPUT_NBEST_PROTOCOL = _bds.EPROTOCOL_INPUT_NBEST_PROTOCOL

_bds.EPROTOCOL_POST_PROTOCOL_swigconstant(_bds)
EPROTOCOL_POST_PROTOCOL = _bds.EPROTOCOL_POST_PROTOCOL

_bds.EPROTOCOL_WISE_PROTOCOL_swigconstant(_bds)
EPROTOCOL_WISE_PROTOCOL = _bds.EPROTOCOL_WISE_PROTOCOL

_bds.EPROTOCOL_WISE_TEXT_PROTOCOL_swigconstant(_bds)
EPROTOCOL_WISE_TEXT_PROTOCOL = _bds.EPROTOCOL_WISE_TEXT_PROTOCOL

_bds.EPROTOCOL_AUDIO_DA_PROTOCOL_swigconstant(_bds)
EPROTOCOL_AUDIO_DA_PROTOCOL = _bds.EPROTOCOL_AUDIO_DA_PROTOCOL

_bds.EPROTOCOL_NLU_PROTOCOL_swigconstant(_bds)
EPROTOCOL_NLU_PROTOCOL = _bds.EPROTOCOL_NLU_PROTOCOL

_bds.EPROTOCOL_NLU_TEXT_PROTOCOL_swigconstant(_bds)
EPROTOCOL_NLU_TEXT_PROTOCOL = _bds.EPROTOCOL_NLU_TEXT_PROTOCOL

_bds.EPROTOCOL_WISE_NLU_PROTOCOL_swigconstant(_bds)
EPROTOCOL_WISE_NLU_PROTOCOL = _bds.EPROTOCOL_WISE_NLU_PROTOCOL

_bds.EPROTOCOL_TALK_PROTOCOL_swigconstant(_bds)
EPROTOCOL_TALK_PROTOCOL = _bds.EPROTOCOL_TALK_PROTOCOL

_bds.EPROTOCOL_SEARCH_MUSIC_PROTOCOL_swigconstant(_bds)
EPROTOCOL_SEARCH_MUSIC_PROTOCOL = _bds.EPROTOCOL_SEARCH_MUSIC_PROTOCOL

_bds.EVRDebugLogLevelOff_swigconstant(_bds)
EVRDebugLogLevelOff = _bds.EVRDebugLogLevelOff

_bds.EVRDebugLogLevelFatal_swigconstant(_bds)
EVRDebugLogLevelFatal = _bds.EVRDebugLogLevelFatal

_bds.EVRDebugLogLevelError_swigconstant(_bds)
EVRDebugLogLevelError = _bds.EVRDebugLogLevelError

_bds.EVRDebugLogLevelWarning_swigconstant(_bds)
EVRDebugLogLevelWarning = _bds.EVRDebugLogLevelWarning

_bds.EVRDebugLogLevelInformation_swigconstant(_bds)
EVRDebugLogLevelInformation = _bds.EVRDebugLogLevelInformation

_bds.EVRDebugLogLevelDebug_swigconstant(_bds)
EVRDebugLogLevelDebug = _bds.EVRDebugLogLevelDebug

_bds.EVRDebugLogLevelTrace_swigconstant(_bds)
EVRDebugLogLevelTrace = _bds.EVRDebugLogLevelTrace

_bds.EVoiceRecognitionClientWorkStatusStartWorkIng_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusStartWorkIng = _bds.EVoiceRecognitionClientWorkStatusStartWorkIng

_bds.EVoiceRecognitionClientWorkStatusStart_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusStart = _bds.EVoiceRecognitionClientWorkStatusStart

_bds.EVoiceRecognitionClientWorkStatusEnd_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusEnd = _bds.EVoiceRecognitionClientWorkStatusEnd

_bds.EVoiceRecognitionClientWorkStatusNewRecordData_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusNewRecordData = _bds.EVoiceRecognitionClientWorkStatusNewRecordData

_bds.EVoiceRecognitionClientWorkStatusFlushData_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusFlushData = _bds.EVoiceRecognitionClientWorkStatusFlushData

_bds.EVoiceRecognitionClientWorkStatusFinish_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusFinish = _bds.EVoiceRecognitionClientWorkStatusFinish

_bds.EVoiceRecognitionClientWorkStatusMeterLevel_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusMeterLevel = _bds.EVoiceRecognitionClientWorkStatusMeterLevel

_bds.EVoiceRecognitionClientWorkStatusCancel_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusCancel = _bds.EVoiceRecognitionClientWorkStatusCancel

_bds.EVoiceRecognitionClientWorkStatusError_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusError = _bds.EVoiceRecognitionClientWorkStatusError

_bds.EVoiceRecognitionClientWorkStatusLoaded_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusLoaded = _bds.EVoiceRecognitionClientWorkStatusLoaded

_bds.EVoiceRecognitionClientWorkStatusUnLoaded_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusUnLoaded = _bds.EVoiceRecognitionClientWorkStatusUnLoaded

_bds.EVoiceRecognitionClientWorkStatusChunkThirdData_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusChunkThirdData = _bds.EVoiceRecognitionClientWorkStatusChunkThirdData

_bds.EVoiceRecognitionClientWorkStatusChunkVPRes_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusChunkVPRes = _bds.EVoiceRecognitionClientWorkStatusChunkVPRes

_bds.EVoiceRecognitionClientWorkStatusChunkNlu_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusChunkNlu = _bds.EVoiceRecognitionClientWorkStatusChunkNlu

_bds.EVoiceRecognitionClientWorkStatusChunkEnd_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusChunkEnd = _bds.EVoiceRecognitionClientWorkStatusChunkEnd

_bds.EVoiceRecognitionClientWorkStatusFeedback_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusFeedback = _bds.EVoiceRecognitionClientWorkStatusFeedback

_bds.EVoiceRecognitionClientWorkStatusRecorderEnd_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusRecorderEnd = _bds.EVoiceRecognitionClientWorkStatusRecorderEnd

_bds.EVoiceRecognitionClientWorkStatusLongSpeechEnd_swigconstant(_bds)
EVoiceRecognitionClientWorkStatusLongSpeechEnd = _bds.EVoiceRecognitionClientWorkStatusLongSpeechEnd

_bds.EVR_STRATEGY_ONLINE_swigconstant(_bds)
EVR_STRATEGY_ONLINE = _bds.EVR_STRATEGY_ONLINE

_bds.EVR_STRATEGY_OFFLINE_swigconstant(_bds)
EVR_STRATEGY_OFFLINE = _bds.EVR_STRATEGY_OFFLINE

_bds.EVR_STRATEGY_ONLINE_PRI_swigconstant(_bds)
EVR_STRATEGY_ONLINE_PRI = _bds.EVR_STRATEGY_ONLINE_PRI

_bds.EVR_STRATEGY_OFFLINE_PRI_swigconstant(_bds)
EVR_STRATEGY_OFFLINE_PRI = _bds.EVR_STRATEGY_OFFLINE_PRI

_bds.EVR_STRATEGY_BOTH_swigconstant(_bds)
EVR_STRATEGY_BOTH = _bds.EVR_STRATEGY_BOTH

_bds.EVR_OFFLINE_ENGINE_INPUT_swigconstant(_bds)
EVR_OFFLINE_ENGINE_INPUT = _bds.EVR_OFFLINE_ENGINE_INPUT

_bds.EVR_OFFLINE_ENGINE_NAVI_swigconstant(_bds)
EVR_OFFLINE_ENGINE_NAVI = _bds.EVR_OFFLINE_ENGINE_NAVI

_bds.EVR_OFFLINE_ENGINE_GRAMMER_swigconstant(_bds)
EVR_OFFLINE_ENGINE_GRAMMER = _bds.EVR_OFFLINE_ENGINE_GRAMMER

_bds.EVR_RESULT_TYPE_ERROR_swigconstant(_bds)
EVR_RESULT_TYPE_ERROR = _bds.EVR_RESULT_TYPE_ERROR

_bds.EVR_RESULT_TYPE_EMPTY_swigconstant(_bds)
EVR_RESULT_TYPE_EMPTY = _bds.EVR_RESULT_TYPE_EMPTY

_bds.EVR_RESULT_TYPE_PARTIAL_swigconstant(_bds)
EVR_RESULT_TYPE_PARTIAL = _bds.EVR_RESULT_TYPE_PARTIAL

_bds.EVR_RESULT_TYPE_NBEST_swigconstant(_bds)
EVR_RESULT_TYPE_NBEST = _bds.EVR_RESULT_TYPE_NBEST

_bds.EVR_RESULT_TYPE_CN_swigconstant(_bds)
EVR_RESULT_TYPE_CN = _bds.EVR_RESULT_TYPE_CN

_bds.EVR_RESULT_TYPE_RESOURCE_swigconstant(_bds)
EVR_RESULT_TYPE_RESOURCE = _bds.EVR_RESULT_TYPE_RESOURCE

_bds.EVR_RESULT_TYPE_THIRD_swigconstant(_bds)
EVR_RESULT_TYPE_THIRD = _bds.EVR_RESULT_TYPE_THIRD

_bds.EVR_RESULT_TYPE_FINISH_swigconstant(_bds)
EVR_RESULT_TYPE_FINISH = _bds.EVR_RESULT_TYPE_FINISH

_bds.EVR_RESULT_TYPE_END_swigconstant(_bds)
EVR_RESULT_TYPE_END = _bds.EVR_RESULT_TYPE_END

_bds.EVR_RESULT_TYPE_VP_RES_swigconstant(_bds)
EVR_RESULT_TYPE_VP_RES = _bds.EVR_RESULT_TYPE_VP_RES

_bds.EVR_NETWORK_TYPE_NO_swigconstant(_bds)
EVR_NETWORK_TYPE_NO = _bds.EVR_NETWORK_TYPE_NO

_bds.EVR_NETWORK_TYPE_2G_swigconstant(_bds)
EVR_NETWORK_TYPE_2G = _bds.EVR_NETWORK_TYPE_2G

_bds.EVR_NETWORK_TYPE_3G_swigconstant(_bds)
EVR_NETWORK_TYPE_3G = _bds.EVR_NETWORK_TYPE_3G

_bds.EVR_NETWORK_TYPE_4G_swigconstant(_bds)
EVR_NETWORK_TYPE_4G = _bds.EVR_NETWORK_TYPE_4G

_bds.EVR_NETWORK_TYPE_WIFI_swigconstant(_bds)
EVR_NETWORK_TYPE_WIFI = _bds.EVR_NETWORK_TYPE_WIFI

_bds.EVR_AUDIO_COMPRESSION_MIN_swigconstant(_bds)
EVR_AUDIO_COMPRESSION_MIN = _bds.EVR_AUDIO_COMPRESSION_MIN

_bds.EVR_AUDIO_COMPRESSION_PCM_swigconstant(_bds)
EVR_AUDIO_COMPRESSION_PCM = _bds.EVR_AUDIO_COMPRESSION_PCM

_bds.EVR_AUDIO_COMPRESSION_BV32_swigconstant(_bds)
EVR_AUDIO_COMPRESSION_BV32 = _bds.EVR_AUDIO_COMPRESSION_BV32

_bds.EVR_AUDIO_COMPRESSION_AMR_swigconstant(_bds)
EVR_AUDIO_COMPRESSION_AMR = _bds.EVR_AUDIO_COMPRESSION_AMR

_bds.EVR_AUDIO_COMPRESSION_MAX_swigconstant(_bds)
EVR_AUDIO_COMPRESSION_MAX = _bds.EVR_AUDIO_COMPRESSION_MAX

_bds.EVRClientErrorDomainRecord_swigconstant(_bds)
EVRClientErrorDomainRecord = _bds.EVRClientErrorDomainRecord

_bds.EVRClientErrorDomainVAD_swigconstant(_bds)
EVRClientErrorDomainVAD = _bds.EVRClientErrorDomainVAD

_bds.EVRClientErrorDomainOnline_swigconstant(_bds)
EVRClientErrorDomainOnline = _bds.EVRClientErrorDomainOnline

_bds.EVRClientErrorDomainLocalNetwork_swigconstant(_bds)
EVRClientErrorDomainLocalNetwork = _bds.EVRClientErrorDomainLocalNetwork

_bds.EVRClientErrorDomainHTTP_swigconstant(_bds)
EVRClientErrorDomainHTTP = _bds.EVRClientErrorDomainHTTP

_bds.EVRClientErrorDomainServer_swigconstant(_bds)
EVRClientErrorDomainServer = _bds.EVRClientErrorDomainServer

_bds.EVRClientErrorDomainOffline_swigconstant(_bds)
EVRClientErrorDomainOffline = _bds.EVRClientErrorDomainOffline

_bds.EVRClientErrorDomainCommon_swigconstant(_bds)
EVRClientErrorDomainCommon = _bds.EVRClientErrorDomainCommon

_bds.EVRClientErrorCodeRecoderException_swigconstant(_bds)
EVRClientErrorCodeRecoderException = _bds.EVRClientErrorCodeRecoderException

_bds.EVRClientErrorCodeRecoderNoPermission_swigconstant(_bds)
EVRClientErrorCodeRecoderNoPermission = _bds.EVRClientErrorCodeRecoderNoPermission

_bds.EVRClientErrorCodeRecoderUnAvailable_swigconstant(_bds)
EVRClientErrorCodeRecoderUnAvailable = _bds.EVRClientErrorCodeRecoderUnAvailable

_bds.EVRClientErrorCodeInterruption_swigconstant(_bds)
EVRClientErrorCodeInterruption = _bds.EVRClientErrorCodeInterruption

_bds.EVRClientErrorCodeVADException_swigconstant(_bds)
EVRClientErrorCodeVADException = _bds.EVRClientErrorCodeVADException

_bds.EVRClientErrorCodeNoSpeech_swigconstant(_bds)
EVRClientErrorCodeNoSpeech = _bds.EVRClientErrorCodeNoSpeech

_bds.EVRClientErrorCodeShort_swigconstant(_bds)
EVRClientErrorCodeShort = _bds.EVRClientErrorCodeShort

_bds.EVRClientErrorCodeOnlineExceptioin_swigconstant(_bds)
EVRClientErrorCodeOnlineExceptioin = _bds.EVRClientErrorCodeOnlineExceptioin

_bds.EVRClientErrorCodeOnlineNetworkUnavailable_swigconstant(_bds)
EVRClientErrorCodeOnlineNetworkUnavailable = _bds.EVRClientErrorCodeOnlineNetworkUnavailable

_bds.EVRClientErrorCodeOnlineTokenFailed_swigconstant(_bds)
EVRClientErrorCodeOnlineTokenFailed = _bds.EVRClientErrorCodeOnlineTokenFailed

_bds.EVRClientErrorCodeOnlineResolveUrlFailed_swigconstant(_bds)
EVRClientErrorCodeOnlineResolveUrlFailed = _bds.EVRClientErrorCodeOnlineResolveUrlFailed

_bds.EVRClientErrorCodeLocalTimeout_swigconstant(_bds)
EVRClientErrorCodeLocalTimeout = _bds.EVRClientErrorCodeLocalTimeout

_bds.EVRClientErrorCodeServerParamError_swigconstant(_bds)
EVRClientErrorCodeServerParamError = _bds.EVRClientErrorCodeServerParamError

_bds.EVRClientErrorCodeServerRecognError_swigconstant(_bds)
EVRClientErrorCodeServerRecognError = _bds.EVRClientErrorCodeServerRecognError

_bds.EVRClientErrorCodeServerNoFindResult_swigconstant(_bds)
EVRClientErrorCodeServerNoFindResult = _bds.EVRClientErrorCodeServerNoFindResult

_bds.EVRClientErrorCodeServerAppNameUnknownError_swigconstant(_bds)
EVRClientErrorCodeServerAppNameUnknownError = _bds.EVRClientErrorCodeServerAppNameUnknownError

_bds.EVRClientErrorCodeServerSpeechQualityProblem_swigconstant(_bds)
EVRClientErrorCodeServerSpeechQualityProblem = _bds.EVRClientErrorCodeServerSpeechQualityProblem

_bds.EVRClientErrorCodeServerSpeechTooLong_swigconstant(_bds)
EVRClientErrorCodeServerSpeechTooLong = _bds.EVRClientErrorCodeServerSpeechTooLong

_bds.EVRClientErrorCodeServerSpeechParamsUnknow_swigconstant(_bds)
EVRClientErrorCodeServerSpeechParamsUnknow = _bds.EVRClientErrorCodeServerSpeechParamsUnknow

_bds.EVRClientErrorCodeServerSpeechNoUploadLink_swigconstant(_bds)
EVRClientErrorCodeServerSpeechNoUploadLink = _bds.EVRClientErrorCodeServerSpeechNoUploadLink

_bds.EVRClientErrorCodeCommonBusy_swigconstant(_bds)
EVRClientErrorCodeCommonBusy = _bds.EVRClientErrorCodeCommonBusy

_bds.EVRClientErrorCodeCommonPropertyListInvalid_swigconstant(_bds)
EVRClientErrorCodeCommonPropertyListInvalid = _bds.EVRClientErrorCodeCommonPropertyListInvalid

_bds.EVRClientErrorCodeCommonEnqueueError_swigconstant(_bds)
EVRClientErrorCodeCommonEnqueueError = _bds.EVRClientErrorCodeCommonEnqueueError

_bds.EVR_MODE_MULTI_SENTENCE_swigconstant(_bds)
EVR_MODE_MULTI_SENTENCE = _bds.EVR_MODE_MULTI_SENTENCE

_bds.EVR_MODE_SINGLE_SENTENCE_swigconstant(_bds)
EVR_MODE_SINGLE_SENTENCE = _bds.EVR_MODE_SINGLE_SENTENCE

_bds.EVR_MODE_MUSIC_swigconstant(_bds)
EVR_MODE_MUSIC = _bds.EVR_MODE_MUSIC

_bds.EVR_MODE_SHAKE_swigconstant(_bds)
EVR_MODE_SHAKE = _bds.EVR_MODE_SHAKE

def asr_request_parse_file(in_file_name):
    return _bds.asr_request_parse_file(in_file_name)
asr_request_parse_file = _bds.asr_request_parse_file
# This file is compatible with both classic and new-style classes.

SDK_TYPE_ASR = cvar.SDK_TYPE_ASR
ASR_CMD_CONFIG = cvar.ASR_CMD_CONFIG
ASR_CMD_START = cvar.ASR_CMD_START
ASR_CMD_PUSH_AUDIO = cvar.ASR_CMD_PUSH_AUDIO
ASR_CMD_STOP = cvar.ASR_CMD_STOP
ASR_CMD_CANCEL = cvar.ASR_CMD_CANCEL
ASR_CMD_KWS_LOAD = cvar.ASR_CMD_KWS_LOAD
ASR_CMD_KWS_UNLOAD = cvar.ASR_CMD_KWS_UNLOAD
BDS_COMMAND_SET_WRITABLE_LIBRARY_DATA_PATH = cvar.BDS_COMMAND_SET_WRITABLE_LIBRARY_DATA_PATH
asr_callback_name = cvar.asr_callback_name
CALLBACK_ASR_STATUS = cvar.CALLBACK_ASR_STATUS
CALLBACK_ASR_RESULT = cvar.CALLBACK_ASR_RESULT
CALLBACK_ASR_LEVEL = cvar.CALLBACK_ASR_LEVEL
CALLBACK_ERROR_DESC = cvar.CALLBACK_ERROR_DESC
CALLBACK_ERROR_CODE = cvar.CALLBACK_ERROR_CODE
CALLBACK_ERROR_DOMAIN = cvar.CALLBACK_ERROR_DOMAIN
CALLBACK_ERROR_SERIAL_NUM = cvar.CALLBACK_ERROR_SERIAL_NUM
ASR_PARAM_KEY_CHUNK_KEY = cvar.ASR_PARAM_KEY_CHUNK_KEY
ASR_PARAM_KEY_CUID = cvar.ASR_PARAM_KEY_CUID
ASR_PARAM_KEY_CHUNK_PARAM = cvar.ASR_PARAM_KEY_CHUNK_PARAM
ASR_PARAM_KEY_CHUNK_ENABLE = cvar.ASR_PARAM_KEY_CHUNK_ENABLE
ASR_PARAM_KEY_ENABLE_LONG_SPEECH = cvar.ASR_PARAM_KEY_ENABLE_LONG_SPEECH
BDS_PARAM_KEY_WRITABLE_LIBRARY_DATA_PATH = cvar.BDS_PARAM_KEY_WRITABLE_LIBRARY_DATA_PATH
ASR_PARAM_KEY_SAVE_AUDIO_ENABLE = cvar.ASR_PARAM_KEY_SAVE_AUDIO_ENABLE
ASR_PARAM_KEY_SAVE_AUDIO_PATH = cvar.ASR_PARAM_KEY_SAVE_AUDIO_PATH
ASR_PARAM_KEY_REALTIME_DATA = cvar.ASR_PARAM_KEY_REALTIME_DATA
COMMON_PARAM_KEY_DEBUG_LOG_LEVEL = cvar.COMMON_PARAM_KEY_DEBUG_LOG_LEVEL
MIC_PARAM_KEY_AUDIO_FILE_PATH = cvar.MIC_PARAM_KEY_AUDIO_FILE_PATH
MIC_PARAM_KEY_NEED_CACHE = cvar.MIC_PARAM_KEY_NEED_CACHE
MIC_PARAM_KEY_DISABLE_AUDIO_OPERATION = cvar.MIC_PARAM_KEY_DISABLE_AUDIO_OPERATION
ASR_PARAM_KEY_SDK_VERSION = cvar.ASR_PARAM_KEY_SDK_VERSION
ASR_PARAM_KEY_START_TONE = cvar.ASR_PARAM_KEY_START_TONE
ASR_PARAM_KEY_STRATEGY = cvar.ASR_PARAM_KEY_STRATEGY
ASR_PARAM_KEY_SAMPLE_RATE = cvar.ASR_PARAM_KEY_SAMPLE_RATE
ASR_PARAM_KEY_MAX_SPEECH_PAUSE = cvar.ASR_PARAM_KEY_MAX_SPEECH_PAUSE
ASR_PARAM_KEY_MAX_WAIT_DURATION = cvar.ASR_PARAM_KEY_MAX_WAIT_DURATION
ASR_PARAM_KEY_MFE_DNN_DAT_FILE = cvar.ASR_PARAM_KEY_MFE_DNN_DAT_FILE
ASR_PARAM_KEY_MFE_CMVN_DAT_FILE = cvar.ASR_PARAM_KEY_MFE_CMVN_DAT_FILE
ASR_PARAM_KEY_DISABLE_PUNCTUATION = cvar.ASR_PARAM_KEY_DISABLE_PUNCTUATION
ASR_PARAM_KEY_ENABLE_SERVER_VAD = cvar.ASR_PARAM_KEY_ENABLE_SERVER_VAD
ASR_PARAM_KEY_ENABLE_CONTACTS = cvar.ASR_PARAM_KEY_ENABLE_CONTACTS
ASR_PARAM_KEY_ENABLE_EARLY_RETURN = cvar.ASR_PARAM_KEY_ENABLE_EARLY_RETURN
ASR_PARAM_KEY_SECRET_KEY = cvar.ASR_PARAM_KEY_SECRET_KEY
ASR_PARAM_KEY_SERVER_URL = cvar.ASR_PARAM_KEY_SERVER_URL
ASR_PARAM_KEY_BROWSER_USER_AGENT = cvar.ASR_PARAM_KEY_BROWSER_USER_AGENT
ASR_PARAM_KEY_APP_ID = cvar.ASR_PARAM_KEY_APP_ID
ASR_PARAM_KEY_VP_PARAMS = cvar.ASR_PARAM_KEY_VP_PARAMS
ASR_PARAM_KEY_API_KEY = cvar.ASR_PARAM_KEY_API_KEY
ASR_PARAM_KEY_PROPERTY_LIST = cvar.ASR_PARAM_KEY_PROPERTY_LIST
ASR_PARAM_KEY_PRODUCT_ID = cvar.ASR_PARAM_KEY_PRODUCT_ID
ASR_PARAM_KEY_CITY_ID = cvar.ASR_PARAM_KEY_CITY_ID
ASR_PARAM_KEY_PROTOCOL = cvar.ASR_PARAM_KEY_PROTOCOL
ASR_PARAM_KEY_LANGUAGE = cvar.ASR_PARAM_KEY_LANGUAGE
ASR_PARAM_KEY_ENABLE_NLU = cvar.ASR_PARAM_KEY_ENABLE_NLU
ASR_PARAM_KEY_ENABLE_LOCAL_VAD = cvar.ASR_PARAM_KEY_ENABLE_LOCAL_VAD
ASR_PARAM_KEY_ENABLE_MODEL_VAD = cvar.ASR_PARAM_KEY_ENABLE_MODEL_VAD
ASR_PARAM_KEY_MODEL_VAD_DAT_FILE = cvar.ASR_PARAM_KEY_MODEL_VAD_DAT_FILE
ASR_PARAM_KEY_COMPRESSION_TYPE = cvar.ASR_PARAM_KEY_COMPRESSION_TYPE
ASR_PARAM_KEY_ENABLE_DRC = cvar.ASR_PARAM_KEY_ENABLE_DRC
ASR_PARAM_KEY_PAM = cvar.ASR_PARAM_KEY_PAM
ASR_PARAM_KEY_STC = cvar.ASR_PARAM_KEY_STC
ASR_PARAM_KEY_LTP = cvar.ASR_PARAM_KEY_LTP
ASR_PARAM_KEY_TXT = cvar.ASR_PARAM_KEY_TXT
ASR_PARAM_KEY_BUA = cvar.ASR_PARAM_KEY_BUA
ASR_PARAM_KEY_NETWORK_STATUS = cvar.ASR_PARAM_KEY_NETWORK_STATUS
ASR_PARAM_KEY_APP = cvar.ASR_PARAM_KEY_APP
ASR_PARAM_KEY_PLATFORM = cvar.ASR_PARAM_KEY_PLATFORM
ASR_PARAM_KEY_COK = cvar.ASR_PARAM_KEY_COK
ASR_PARAM_KEY_PU = cvar.ASR_PARAM_KEY_PU
ASR_PARAM_KEY_FRM = cvar.ASR_PARAM_KEY_FRM
ASR_PARAM_KEY_RSV = cvar.ASR_PARAM_KEY_RSV
OFFLINE_PARAM_KEY_APP_CODE = cvar.OFFLINE_PARAM_KEY_APP_CODE
OFFLINE_PARAM_KEY_LICENSE_FILE_PATH = cvar.OFFLINE_PARAM_KEY_LICENSE_FILE_PATH
ASR_PARAM_KEY_OFFLINE_ENGINE_TYPE = cvar.ASR_PARAM_KEY_OFFLINE_ENGINE_TYPE
ASR_PARAM_KEY_OFFLINE_ENGINE_DAT_FILE_PATH = cvar.ASR_PARAM_KEY_OFFLINE_ENGINE_DAT_FILE_PATH
ASR_PARAM_KEY_OFFLINE_ENGINE_GRAMMER_FILE_PATH = cvar.ASR_PARAM_KEY_OFFLINE_ENGINE_GRAMMER_FILE_PATH
ASR_PARAM_KEY_OFFLINE_ENGINE_GRAMMER_SLOT = cvar.ASR_PARAM_KEY_OFFLINE_ENGINE_GRAMMER_SLOT
ASR_PARAM_KEY_OFFLINE_ENGINE_WAKEUP_WORDS_FILE_PATH = cvar.ASR_PARAM_KEY_OFFLINE_ENGINE_WAKEUP_WORDS_FILE_PATH
ASR_PARAM_KEY_OFFLINE_ENGINE_TRIGGERED_WAKEUP_WORD = cvar.ASR_PARAM_KEY_OFFLINE_ENGINE_TRIGGERED_WAKEUP_WORD
PARAM_TYPE_MAX_ASR_INSTANCE_NUM = cvar.PARAM_TYPE_MAX_ASR_INSTANCE_NUM

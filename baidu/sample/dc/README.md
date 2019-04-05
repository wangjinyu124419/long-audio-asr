# ASR API for DC



注意：确保../../resources/asr_resource/bds_easr_mfe_dnn.dat文件的存在。

1.进入python3的虚拟环境
source /home/xqw/py3env/bin/activate
2.编译：
$make
3.测试：
运行python，调用：
result=bds.asr_request_parse_file("/home/xqw/work/baidu/sample/asr/pcm/16k-0.pcm")



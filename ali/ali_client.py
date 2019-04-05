import os
import time

from ali.ali_sdk import fileTrans
import  json
accessKeyId = "LTAIlkMstf8ykrRf"
accessKeySecret = "Wndz12Ct0phoIsnD3yYaVCIbllMLhq"
appKey = "LiXNBmUZPXYsBKsv"

# fileLink = "https://aliyun-nls.oss-cn-hangzhou.aliyuncs.com/asr/fileASR/examples/nls-sample-16k.wav"

# 执行录音文件识别

def get_result(fileLink):
    getResponse=fileTrans(accessKeyId, accessKeySecret, appKey, fileLink)
    print((getResponse))
    # res=json.dumps(getResponse,indent=4,ensure_ascii=False)
    # print(res)
    Sentences_list=getResponse['Result']['Sentences']
    res=''
    for sentence in Sentences_list:
        res+=sentence.get('Text')
    # print(res)
    return res
    # print(Sentences_list)
    # print(type(res))


if __name__ == '__main__':

    base_url='https://www.shenducurious.cn/audio/mp3'
    files_path='/home/wangjinyu/workproject/long_audio_asr/mp3_audio'
    files_list=os.listdir(files_path)

    f = open(os.path.join('/home/wangjinyu/workproject/long_audio_asr/mp3_audio', 'ali.txt'), 'a')
    for file in files_list:
        if not file.endswith('wav'):
            continue
        new_link = os.path.join(base_url,file)
        print(new_link)
        res = get_result(new_link)
        print(res)
        f.write(file + ':' + res + '\n')


    # fp=open('/home/wangjinyu/workproject/long_audio_asr/res/result/txt/video_ali_heima.txt', 'a')
    #
    # # fileLink = "https://www.shenducurious.cn/audio/long_audio/audio_guo/0.wav"
    # s_time=time.time()
    # for i in range(10):
    #     fileLink="https://www.shenducurious.cn/audio/long_audio/one_minute/60s_{}.wav".format(str(i))
    #     print(fileLink)
    #     res=get_result(fileLink)
    #     print(res)
    #     if res:
    #         fp.write(res+'\n')
    #
    # e_time=time.time()
    # t_time=e_time-s_time
    # print('总耗时：%r',t_time)

    # print(res)
    #

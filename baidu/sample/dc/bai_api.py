import os
import json
import time
import bds

# import pprint
# res=bds.asr_request_parse_file('/home/wangjinyu/workproject/baidu/sample/asr/pcm/16k-0.pcm')
# res = bds.asr_request_parse_file('/home/wangjinyu/workproject/baidu/sample/asr/pcm/16k-1.pcm')
# res = bds.asr_request_parse_file('/home/wangjinyu/workproject/baidu/sample/dc/middle_wav/wav_25s_0.wav')
files_path='/home/wangjinyu/workproject/baidu/audio/pcm'
files_path='/home/wangjinyu/workproject/baidu/audio/xufeihecheng/audio'
files_path='/home/wangjinyu/workproject/baidu/audio/xufeihecheng/audio_guo'
files_path='/home/wangjinyu/workproject/long_audio_asr/res/xufeihecheng/audio_python'
file_list=os.listdir(files_path)

def get_result(file_path):
    res = bds.asr_request_parse_file(file_path)
    total_str=''
    str_list=res.split('}{')
    # print(str_list)
    for str in str_list:
        if len(str_list)>1:
            # print('----------',str)
            if str==str_list[0]:
                str=str+"}"
            elif str==str_list[-1]:
                str="{"+str
            else:
                str="{"+str+"}"
        # print('--------------',str)
        #
        temp_str=json.loads(str).get('results_recognition')[0]
        total_str+=temp_str
    print('-----------',total_str)
    return total_str


if __name__ == '__main__':

    import os

    files_path = '/home/wangjinyu/workproject/long_audio_asr/mp3_audio'

    files_list = os.listdir(files_path)
    f = open(os.path.join(files_path, 'baidu.txt'), 'a')
    for file in files_list:
        if not file.endswith('wav'):
            continue
        file_path = os.path.join(files_path, file)
        print(file_path)
        res = get_result(file_path)
        print(res)
        f.write(file + ':' + res + '\n')

        time.sleep(2)

    # get_result('/home/wangjinyu/workproject/long_audio_asr/res/real_wav/xuexiangchong/xuexiangchong5.wav')

    # fp=open('xunfei_baidu_guo.txt','a')
    # s_time=time.time()
    # for i in range(len(file_list)):
    #     file=str(i)+"."+"wav"
    #     print(file)
    #     file_path=os.path.join(files_path,file)
    #     with open(file_path,'rb') as f:
    #         content=f.read()[44:]
    #     with open('temp.pcm','wb') as f2:
    #         f2.write(content)
    #
    #     text=get_result('temp.pcm')
    #     if text:
    #         fp.write(text+'\n')
    # e_time=time.time()
    # t_time=e_time-s_time
    # print('百度总耗时：%s',t_time)





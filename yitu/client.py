
from sample import get_result

# res=get_result('/home/wangjinyu/workproject/long_audio_asr/res/real_wav/xuexiangchong/xuexiangchong5.wav')
import os

files_path='/home/wangjinyu/workproject/long_audio_asr/mp3_audio'

files_list=os.listdir(files_path)
f=open(os.path.join(files_path,'yitu.txt'),'a')
for file in files_list:
    file_path=os.path.join(files_path,file)
    res=get_result(file_path)
    f.write(file+':'+res+'\n')

#
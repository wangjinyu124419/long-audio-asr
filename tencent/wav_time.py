import  wave

f=wave.open('/home/wangjinyu/workproject/long_audio_asr/res/one_minute/60s_0.wav','r')
nframe=f.getnframes()
frame=f.getframerate()
print(nframe//frame)


with open('https://www.shenducurious.cn/audio/tencent/1.txt','rb') as f:
    print(f.read())

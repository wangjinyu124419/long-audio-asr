import time

from xunfei.weblfasr_python3_demo import RequestApi
import  json
appid="5c458f95"
secret_key="8c6cc2043040a13ff36c5ead9349c530"

def get_result(file_path):

    api = RequestApi(appid=appid, secret_key=secret_key,upload_file_path=file_path)
    response=api.all_api_request()
    # data={ 'data': '[{"bg":"7140","ed":"10380","onebest":"我会先对其父亲说，","speaker":"0"},{"bg":"10400","ed":"11880","onebest":"节哀顺变，","speaker":"0"},{"bg":"13350","ed":"14870","onebest":"询问下","speaker":"0"},{"bg":"14890","ed":"18240","onebest":"什么时间的事情，什么原因？","speaker":"0"},{"bg":"37260","ed":"39960","onebest":"然后请其父亲","speaker":"0"},{"bg":"40100","ed":"42350","onebest":"提交我方一份，","speaker":"0"},{"bg":"42590","ed":"43920","onebest":"死者的死亡！","speaker":"0"},{"bg":"43930","ed":"45090","onebest":"证明，","speaker":"0"},{"bg":"45730","ed":"49540","onebest":"告诉其父亲联系地址，","speaker":"0"},{"bg":"50160","ed":"53580","onebest":"我放好进下一步处理。","speaker":"0"},{"bg":"54430","ed":"56740","onebest":"如果金额不多，","speaker":"0"},{"bg":"57950","ed":"60070","onebest":"会劝家属","speaker":"0"},{"bg":"60090","ed":"62060","onebest":"能否给还上，","speaker":"0"},{"bg":"63970","ed":"67180","onebest":"尽可能的不造成公司。","speaker":"0"},{"bg":"67190","ed":"68710","onebest":"的损失！","speaker":"0"}]', 'err_no': 0, 'failed': None, 'ok': 0}

    data_list=json.loads(response.get('data'))

    res=''.join([ data.get('onebest') for data in data_list])
    return res


if __name__ == '__main__':

    import os

    files_path = '/home/wangjinyu/workproject/long_audio_asr/mp3_audio'

    files_list = os.listdir(files_path)
    f = open(os.path.join(files_path, 'xunfei.txt'), 'a')
    for file in files_list:
        if not file.endswith('wav'):
            continue
        file_path = os.path.join(files_path, file)
        print(file_path)
        res = get_result(file_path)
        print(res)
        f.write(file + ':' + res + '\n')

        time.sleep(2)
    # for i in range(10):
        # file='/home/wangjinyu/workproject/long_audio_asr/res/real_wav/yangqingqing/yangqingqing{}.wav'.format(str(i+1))
        # print(file)
        # res=get_result(file)

        # res=get_result('/home/wangjinyu/workproject/long_audio_asr/res/real_wav/wangsongbo/wangsongbo10.wav')
        # f=open('/home/wangjinyu/workproject/long_audio_asr/res/real_test/wangsongbo/txt/xunfei.txt','a')
        # f.write(res+'\n')
        # print(res)

    # data = {'data': '[{"bg":"7140","ed":"10380","onebest":"我会先对其父亲说，","speaker":"0"},{"bg":"10400","ed":"11880","onebest":"节哀顺变，","speaker":"0"},{"bg":"13350","ed":"14870","onebest":"询问下","speaker":"0"},{"bg":"14890","ed":"18240","onebest":"什么时间的事情，什么原因？","speaker":"0"},{"bg":"37260","ed":"39960","onebest":"然后请其父亲","speaker":"0"},{"bg":"40100","ed":"42350","onebest":"提交我方一份，","speaker":"0"},{"bg":"42590","ed":"43920","onebest":"死者的死亡！","speaker":"0"},{"bg":"43930","ed":"45090","onebest":"证明，","speaker":"0"},{"bg":"45730","ed":"49540","onebest":"告诉其父亲联系地址，","speaker":"0"},{"bg":"50160","ed":"53580","onebest":"我放好进下一步处理。","speaker":"0"},{"bg":"54430","ed":"56740","onebest":"如果金额不多，","speaker":"0"},{"bg":"57950","ed":"60070","onebest":"会劝家属","speaker":"0"},{"bg":"60090","ed":"62060","onebest":"能否给还上，","speaker":"0"},{"bg":"63970","ed":"67180","onebest":"尽可能的不造成公司。","speaker":"0"},{"bg":"67190","ed":"68710","onebest":"的损失！","speaker":"0"}]','err_no': 0, 'failed': None, 'ok': 0}


    # data_list = json.loads(data.get('data'))

    # res = ''.join([data.get('onebest') for data in data_list])

    # dict={'data': '[{"bg":"0","ed":"7470","onebest":"零基础学it，月薪过万就来，黑马程序员，黑马程序员成就it黑马！","speaker":"0"},{"bg":"8170","ed":"14960","onebest":"员基础，啊第一呃这个是CA加学院那个是资源基础第一部分，啊就是咱们的最基础这块内容，啊","speaker":"0"},{"bg":"14980","ed":"21990","onebest":"那首先我们看一下第一个知识体系，啊咱们这个整体去给大家去讲一下，啊这里面有这个网格视图看一下，啊","speaker":"0"},{"bg":"21980","ed":"25370","onebest":"那这里面会分为了这个总共是这个是12块啊11，","speaker":"0"}]', 'err_no': 0, 'failed': None, 'ok': 0}
    # print(type(dict['data'][0]))
    # res = ''.join([(json.loads(data)).get('onebest') for data in dict['data']])
    # data_list=json.loads(dict['data'])
    # print(type(data_list))
    # for data in data_list:
    #     print(data['onebest'])# print(data)

    # print(res)
    # print(json.dumps(dict,indent=4,ensure_ascii=False))

import  requests
# url='http://47.105.69.153:8322'
url='http://localhost:8322'
res=requests.get(url=url,params={'task_id':'1'})
print(res.content.decode('utf-8'))
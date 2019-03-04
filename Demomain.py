import requests,json
from Template.Demolog import *

# class Maintest(object):
#     def ZdPost(self,host,port,url,querystring,payload=None,header=None):
#         global response
#         if header != None:
#             res = requests.request("Post", url=host + port + url, params=querystring, data=json.dumps(payload),
#                                    headers=header, timeout=8, verify=False)
#         else:
#             res = requests.request("Post", url=host + port + url, params=querystring, data=json.dumps(payload),
#                                    timeout=8, verify=False)
#         response = res.content.decode('utf-8')

"""定义Post"""
def TestPost(host,port,url,querystring,payload,header=None):
    global response
    if header!=None:
        res = requests.request("Post", url=host + port + url, params=querystring, data=json.dumps(payload),headers=header,timeout=8,verify=False)
    else:
        res = requests.request("Post", url=host + port + url, params=querystring, data=json.dumps(payload),timeout=8,verify=False)
    response = res.content.decode('utf-8')
    logging.info("接口请求url" + "-" * 20 + ">" * 2 + " %s", res.url)
    logging.info("接口请求data" + "-" * 20 + ">" * 2 + " %s", payload)
    jg=Returncode()
    logging.info("接口请求结果" + "-" * 20 + ">" * 2 + " %s", jg)
    #print(response)
"""定义Get"""
def TestGet(host,port,url,querystring,payload,header=None):
    if header!=None:
        res = requests.request("Get", url=host + port + url, params=querystring, data=json.dumps(payload),headers=header,timeout=8,verify=False)
    else:
        res = requests.request("Get", url=host + port + url, params=querystring, data=json.dumps(payload),timeout=8,verify=False)
    response = res.content.decode('utf-8')
    print(response)
"""定义主体"""
def TestMain(url,querystring,payload=None,method='post',header={'content-type': "application/json"},host='http://172.17.13.74',port=':80'):
    if method=='Post' or 'post':
        response=TestPost(host, port, url, querystring, payload, header)
    else:
        response = TestGet(host, port, url, querystring, payload, header)
    return response
def Token():
    token=json.loads(response)
    return token['data']['token']

"""获取returncode"""
def Returncode():
    returncode=json.loads(response)
    code=returncode['returncode']
    if code == 0 or code == '0':
        print('Pass',response)
        # logging.info("接口请求成功" + "-" * 20 + ">" * 2 + " %s", response)
    else:
        print('Fail', response)
        # logging.debug("接口请求失败" + "-" * 20 + ">" * 2 + " %s", response)
import requests
import json

def gettoken():
    url ='http://192.168.1.124:35357/v2.0/tokens'
    data = {"auth": {"tenantName":"admin","passwordCredentials":{"username":"admin","password":"Welcome123"}}}
    a = requests.post(url,json.dumps(data),headers = {'Content-Type':'application/json'})
    if a.status_code !=200:
        raise Exception("Platform9 login returned %d, body: %s" %(a.status_code, a.text))
    else:
        response = a.json()
        return response

respon = gettoken()
token =  respon['access']['token']['id']

#print token

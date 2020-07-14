from flask import Flask
from flask import request
import json
import requests
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    output="Hello world from method: "+request.method
    return output

@app.route('/master_nodes',methods=['GET'])
def master_nodes():
    url="https://172.16.11.252:6443/api/v1/nodes"
    headers = {"Authorization": "Bearer eyJ6IiJ9.eyJpc3MiOiJrdWZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImFkbWluLXVzZXItdG9rZW4taDhobnYiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiYWRtaW4tdXNlciIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjUzODA2NmY5LWExOGQtMTFlYS04MjQ0LWVjZWJiODk4MDE4OCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmFkbWluLXVzZXIifQ.HggNbSz18K_wttcW93-Cf0TvCEzwQHrpzdc4Ue2Nbs8aqd7NQkAU4OC6WYwwiJKmqODDXE-B2-az7KJD8f_EGKI04kMgShtvc32U0oO_ibRGk-PZKdRRGLQSVb6nHW-JgmsoKGPEFy4n7OiCFB_1jAzcH-G3cK5c3ENTPlANSqs_cPlDTc3hWTL6Usjkqzivw9yyHwJVn8u5-EV4akx6qOs9Zmkv3HcfJtNxa835VEtQ8imhU-zDZ2_0_X1DyMmZZsxwFGiHw-i986VosNMhqweZBM2dc7CXg2i5WEYPmVeE1P-xFFBWgErSqqUGIBpOTHgRNxABTYsTYZ2WXHtYlw"}
    resp=requests.get(url, headers=headers, verify=False).json()
    output=[]
    for i in resp['items']:
     output.append(i['metadata']['name'])

    return str(output)

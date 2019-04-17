# -*- encoding: utf-8 -*-

import requests
import json


d1 = {}
d1['team'] = ''
d1['channel'] = 'wechat,email'
d1['callback_url'] = ''
text = ''
f = open("", "r") 
lines = f.readlines()
for line in lines :
    line = line.decode('utf-8')
    text += line
    text += '\n'
d1['msg'] = text

s = requests.Session()
postdata = json.dumps(d1)
url = "" 
s.post(url = url, timeout = 5, data = postdata)


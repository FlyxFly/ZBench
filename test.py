# -*- coding: UTF-8 -*-
import json
f=open('bt.txt','r')
content=f.read()
result_arr=content.replace('} {','}@@@{').split('@@@')
print json.dumps(result_arr)
f.close()
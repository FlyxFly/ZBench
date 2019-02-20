#coding=utf-8
import json
def fmt(file):
        try:
                f=open(file)
        except:
                print '路由追踪文件不存在'
                return;
        content=f.read()
        f.close()
        content_string_arr=content.split('\n')
        content_arr=list()
        for item in content_string_arr:
                if len(item)>0 :
                        content_arr.append(json.loads(item))
        t=open(file+'_table','w')
        t.write(json.dumps(content_arr))
        t.close()
        
        

fmt("/tmp/shm.txt")
fmt("/tmp/sht.txt")
fmt("/tmp/shu.txt")
fmt("/tmp/gdm.txt")
fmt("/tmp/gdt.txt")
fmt("/tmp/gdu.txt")
fmt("/tmp/cde.txt")
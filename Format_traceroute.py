# coding=utf-8
import json


def fmt(file):
    try:
        f = open(file, 'r')
    except:
        print '路由追踪文件不存在'+file
        return
    content = f.read()
    f.close()
    content_string_arr = content.split('\n')
    content_arr = list()
    for idx, item in enumerate(content_string_arr):
        if len(item) > 0:
            try:
                line = json.loads(item)
            except ValueError:
                print(u'解析Traceroute JSON出错', item)
                continue
            if line.has_key('hop') and line['hop'] < 4:
                line['data'][0]['ip'] = "已隐藏"
            content_arr.append(line)
    t = open(file+'_table', 'w')
    t.write(json.dumps(content_arr))
    t.close()


fmt("/tmp/shm.txt")
fmt("/tmp/sht.txt")
fmt("/tmp/shu.txt")
fmt("/tmp/gdm.txt")
fmt("/tmp/gdt.txt")
fmt("/tmp/gdu.txt")
fmt("/tmp/cde.txt")

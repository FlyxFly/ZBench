#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
 Author 雨落无声（Github: https://github.com/ylws-4617)
 Reference:
 1. https://www.s0nnet.com/archives/python-icmp
 2. http://www.pythoner.com/357.html
'''

import commands
import json

def ping(host):
    cmd = "ping "+ str(host) + " -c2 -W 2"
    result = commands.getoutput(cmd)
    result = result.split()
    result = result[-2].split("/")[0]
    if result.isalpha():
        result = False
    return float(result)


STYLE = {
    'fore': {
        'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
        'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37,
    },
    'back': {
        'black': 40, 'red': 41, 'green': 42, 'yellow': 43,
        'blue': 44, 'purple': 45, 'cyan': 46, 'white': 47,
    },
    'mode': {
        'bold': 1, 'underline': 4, 'blink': 5, 'invert': 7,
    },
    'default': {
        'end': 0,
    }
}


def use_style(string, mode='', fore='', back=''):
    mode = '%s' % STYLE['mode'][mode] if STYLE['mode'].has_key(mode) else ''
    fore = '%s' % STYLE['fore'][fore] if STYLE['fore'].has_key(fore) else ''
    back = '%s' % STYLE['back'][back] if STYLE['back'].has_key(back) else ''
    style = ';'.join([s for s in [mode, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end = '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style, string, end)

D = {
    '郑州': '5ghenan.ha.chinamobile.com',
    '济南': '202.102.152.3',
    '天津': '219.150.32.132',
    '拉萨': 'speedtest1.xz.chinamobile.com:',
    '长春': '202.98.0.68',
    '兰州': 'www.lanzhouunicom.com',
    '西宁': '223.221.77.118',
    '合肥': '112.122.10.26',
    '武汉': 'vipspeedtest4.wuhan.net.cn',
    '重庆': 'speedtest1.cqccn.com',
    '上海': '5g.shunicomtest.com',
    '呼和浩特': '222.74.1.200	',
    '乌鲁木齐': '61.128.114.133',
    '杭州': '122.229.136.10',
    '西安': 'xatest.wo-xa.com',
    '宁波': 'ltetest3.139site.com',
    '苏州': '4gsuzhou1.speedtest.jsinfo.net',
    '长沙': '61.234.254.5',
    '哈尔滨': '202.97.224.1',
    '北京': 'gameeye.huaweicloud.com',
    '成都': 'speedtest1.wangjia.net',
    '南京': '5gnanjing.speedtest.jsinfo.net',
    '宁夏': '221.199.9.35',
    '福州': 'upload1.testspeed.kaopuyun.com',
    '广州': 'gd.189.cn'
    }



string =list()
d=dict()
ping_result=list()
for x in D:
    host=D[x]
    result = ping(host)
    item=dict()
    item['name']=x
    item['latency']=result
    ping_result.append(item)
    # print (x,result);

    if result == False:
        latency_str = use_style(str("Fail"), fore='red')
    elif float(result) <= 60:
        latency_str =use_style(str(round(result,2)) + " ms",fore='green')
    elif float(result) <= 130:
        latency_str = use_style(str(round(result,2))+" ms",fore='yellow')
    else:
        latency_str = use_style(str(round(result,2))+" ms", fore='red')

    d[x] = float(result)

    string.append((x,latency_str))
    if len(string) == 3:
        l1 = str(int(len(string[0][0])/3+12))
        l2 = str(int(len(string[1][0])/3+12))
        l3 = str(int(len(string[2][0])/3+12))
        mystring = "{0:"+l1+"}: {1:20}{2:"+l2+"}: {3:20}{4:"+l3+"}: {5:20}"
        print(mystring.format(string[0][0],string[0][1],string[1][0],string[1][1],string[2][0],string[2][1]))
        string = list()

# print json.dumps(ping_result)
f = open('/tmp/ZBenchping.txt','w')
f.write(json.dumps(ping_result))
f.close()
if len(string) == 2:
    l1 = str(int(len(string[0][0])/3+12))
    l2 = str(int(len(string[1][0])/3+12))
    mystring = "{0:"+l1+"}: {1:20}{2:"+l2+"}: {3:20}"
    print(mystring.format(string[0][0],string[0][1],string[1][0],string[1][1]))

if len(string) == 1:
    l1 = str(int(len(string[0][0])/3+12))
    mystring = "{0:"+l1+"}: {1:20}"
    print(mystring.format(string[0][0],string[0][1]))


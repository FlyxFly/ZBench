#coding=utf-8
import sys
import json

test_result_file=sys.argv[1]
node_name=sys.argv[2]
try:
    f = open(test_result_file, 'r')
except:
    print 'Read reusult file error.' 
    exit()
# test_result='{"client": {"rating": "0", "loggedin": "0", "isprating": "3.7", "ispdlavg": "0", "ip": "107.172.97.115", "isp": "ColoCrossing", "lon": "-78.8781", "ispulavg": "0", "country": "US", "lat": "42.8864"}, "bytes_sent": 8880128, "download": 31257166.368636932, "timestamp": "2019-02-12T03:08:00.675315Z", "share": "http://www.speedtest.net/result/8033040446.png", "bytes_received": 40130595, "ping": 397.661, "upload": 6925880.089663532, "server": {"latency": 397.661, "name": "XiangYang", "url": "http://sp1.xyspeedtest.com:8080/speedtest/upload.php", "country": "China", "lon": "112.1330", "cc": "CN", "host": "sp1.xyspeedtest.com:8080", "sponsor": "China Telecom Xiangyang Branch", "lat": "32.0170", "id": "12637", "d": 11610.856447218877}}'
test_result=f.read()
try:
    speedtest=json.loads(test_result)
except ValueError:
    print test_result
    print 'Error',node_name,test_result
    exit()

upload_speed=round(speedtest['upload']/8388608,2)
download_speed=round(speedtest['download']/8388608,2)
server=speedtest['server']['name']
latency=round(speedtest['ping'],3)
print "{:<30s}{:<20s}{:<22s}{:<8s}".format(node_name,str(upload_speed)+'MB/s',str(download_speed)+'MB/s',str(latency)+'ms')

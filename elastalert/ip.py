#!/usr/bin/python
#_*_coding:utf-8 _*_
#Reference: http://blog.51cto.com/1992mrwang/1206673

import urllib,urllib2
import json
import sys
import simplejson


def ipInfo(ipaddress):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ipaddress
    page = urllib.urlopen(url)
    data = page.read()
    jsondata = json.loads(data)
    if jsondata[u'code'] == 0:
        print ' '
        print '国家：' + jsondata[u'data'][u'country'].encode('utf-8')
        print '地区：' + jsondata[u'data'][u'area'].encode('utf-8')
        print '省份：' + jsondata[u'data'][u'region'].encode('utf-8')
        print '城市：' + jsondata[u'data'][u'city'].encode('utf-8')
        print '运营商：' + jsondata[u'data'][u'isp'].encode('utf-8')
    else:
        print '查询失败 请检查IP 后再说'

if __name__ == '__main__':
    ipaddress = str(sys.argv[1])
    ipInfo(ipaddress)

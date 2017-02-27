# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random

class ProxyMiddleware(object):
    
    def __init__(self):
        
        file = open('GetData_Sina/proxy_ip.txt')
        list = file.readlines()
        self.proxys = list[0].split('|')
    
    def process_request(self, request, spider):
        
        ip = random.choice(self.proxys)
        ip = 'http://'  + ip
        #print('ip:' + ip)
        request.meta['proxy'] = ip
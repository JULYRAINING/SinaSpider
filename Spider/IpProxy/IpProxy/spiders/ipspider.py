# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.selector import Selector

from IpProxy.items import ProxyItem


class IpspiderSpider(scrapy.Spider):
    name = "proxy"
    allowed_domains = ["youdaili.net"]
    

    def start_requests(self):
        
        
        url = 'http://www.youdaili.net/'
        
        yield Request(url = url,  callback = self.parse0)
        
    
    def parse0(self, response):
        
        selector = Selector(response)
        links = selector.re('href="(\S+\d+.html)"')
        
        size = len(links)
        
        for index, link in enumerate(links):
            print('%s in %s', index, size)
            yield Request(url = link,  callback = self.parse1)
            
        
    def parse1(self, response):   
        
        selector = Selector(response) 
        
        proxys = selector.re('(\d+\.\d+\.\d+\.\d+:\d+)')
        
        for proxy in proxys:
            ip, port = proxy.split(':')
            item = ProxyItem()
            item['ip'] = ip
            item['port'] = port
            print(item)
            yield item
    
    
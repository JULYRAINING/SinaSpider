# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.selector.unified import Selector
import os ,re, datetime

class GetdataSpider(scrapy.Spider):
    name = "getData"
    #allowed_domains = ["weibo.com"]
    start_urls = ['http://weibo.com/']

    def start_requests(self):
        
        year = 2015
        #起始日期
        begin_date = datetime.datetime.strptime('2015-1-1', "%Y-%m-%d")
        while year <=2017:
            
            for i in range(1,24):
                year = begin_date.year
                month = begin_date.month
                day = begin_date.day
                hour = i
                url = 'http://s.weibo.com/weibo/%%25E9%%259B%%25BE%%25E9%%259C%%25BE&typeall=1&suball=1&timescope=custom:%(year)s-%(month)s-%(day)s-%(hour)s:%(year)s-%(month)s-%(day)s-%(hour)s&Refer=g' %({'year':year, 'month':month, 'day':day, 'hour':hour})
                #print(url)
                
                yield Request(url = url, callback = self.parse0)
                
            begin_date += datetime.timedelta(days = 1)    
        
        ''' 
        
        for a in range(1, 10):
            url = 'http://httpbin.org/ip?%s' % a
            #url = 'http://s.weibo.com/weibo/%%25E9%%259B%%25BE%%25E9%%259C%%25BE&typeall=1&suball=1&timescope=custom:2017-01-0%s:2017-01-0%s&Refer=g' % (a, a)
            print(url)
            yield Request(url = url, callback = self.parse0)
        '''
    def parse0(self, response):
        path = 'E:/Code/Python/data/data/'
        selector = Selector(response)
        
        if not os.path.exists('data'):
            os.mkdir('data')
        time = re.findall('\d{4}-\d{1,}-\d{1,}-\d{1,}', response.url)
        print(time[0])
        file = open(path + time[0] , 'w')
        file.write(response.body)
        file.close()
        
        
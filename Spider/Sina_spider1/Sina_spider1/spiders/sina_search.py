# -*- coding: utf-8 -*-
import re

import pymongo
import scrapy
from scrapy.http.request import Request
from scrapy.selector.unified import Selector

from Sina_spider1.items import SearchItem


class SinaSearchSpider(scrapy.Spider):
    name = "sina_search"
    allowed_domains = ["weibo.com"]
    start_urls = ['http://weibo.com/']

    def start_requests(self):
        
        url = 'http://s.weibo.com/weibo/%25E9%259B%25BE%25E9%259C%25BE&typeall=1&suball=1&timescope=custom:2017-01-01:2017-01-02&Refer=g'
        cookie = 'SINAGLOBAL=2460208457668.2603.1483357373892; wvr=6; SSOLoginState=1483430940; SWB=usrmdinst_0; _s_tentry=-; Apache=4632757037593.315.1483494311046; ULV=1483494312037:2:2:2:4632757037593.315.1483494311046:1483357373904; SCF=Ahc3WlFibkJSwdZbEvzgNM34q-lYcfvJ6_OMUk-MUeu4D1Zwyj3akrtATa-3OfF0vFN0Qa-iLHHni5CMi1-aIRM.; SUB=_2A251amUYDeRxGeVG6VEW9i7IwzSIHXVWHtHQrDV8PUNbmtANLW7RkW9gqLoddIzEHY3glck9m9hFBGwCJg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWSzG75WaU6Wd_.025ROw535JpX5KMhUgL.FoeReoeNSo5X1hn2dJLoI7_ZUgp4MJ8DdJLV97tt; SUHB=0N2110U7NxGDdY; ALF=1515145416; WBStorage=194a5e7d191964cc|undefined; UOR=,,login.sina.com.cn'
        cookie_dict = dict((line.split('=') for line in cookie.strip().split(";")))
        
        yield Request(url = url,cookies = cookie_dict, callback = self.parse0)
        
    
    def parse0(self, response):
        
        selector = Selector(response)
        print(response)
        text = selector.xpath('//script/text()')[15].extract()
        
        
        result = re.sub(r'\\([^u])', r'\1', text)
        
        
        html = Selector(text = result)
        
        
        client = pymongo.MongoClient('localhost:27017')
        
        db = client['sina_search']
        
        title = db['nickname']
        
        mids = html.xpath('//div[@action-type = "feed_list_item"]/@mid').extract()
        nicknames = html.xpath('//div[@class = "content clearfix"]/div[@class = "feed_content wbcon"]/p/@nick-name').extract()
        profiles = html.xpath('//div[@class = "content clearfix"]/div[@class = "feed_content wbcon"]/a[@class = "W_texta W_fb"]/@href').extract()
        contents = html.xpath('//div[@class = "content clearfix"]/div[@class = "feed_content wbcon"]/p').extract()
        dates = html.xpath('//div[@class = "feed_from W_textb"]/a[@class = "W_textb"]/text()').extract()
        froms = html.xpath('//div[@class = "feed_from W_textb"]/a[@rel = "nofollow"]/text()').extract()
        forwards = html.xpath('//a[@action-type = "feed_list_forward"]/span').xpath('string(.)').extract()
        comments = html.xpath('//a[@action-type = "feed_list_comment"]/span').xpath('string(.)').extract()
        likes = html.xpath('//a[@action-type = "feed_list_like"]/span').xpath('string(.)').extract()
        
        
        profile_vs = html.xpath('//div[@class = "content clearfix"]/div[@class = "feed_content wbcon"]').extract()
        
        validates = []
        
        for item in profile_vs:
            str_item = item.encode('utf-8')
            #官方
            if str_item.find('W_icon icon_approve_co')!=-1:
                validates.append(3) 
            #自媒体   
            elif str_item.find('W_icon icon_approve')!=-1:
                validates.append(2) 
            #个人   
            elif str_item.find('W_icon icon_approve_goldo')!=-1:
                validates.append(1)  
            else:
                 validates.append(0)  

        items = zip(nicknames, profiles, contents, dates, froms, forwards, comments, likes, validates, mids)
        
        
        for i in items:
            item = SearchItem()
            
            item["nickname"] = i[0]
            item["profile"] =  i[1]
            
            item["longpost"] =  0
            
            se = Selector(text = i[2])
            content_value = se.xpath('string(.)').extract()[0]
            item["content"] =  content_value
            
            
            if i[2].find('action-type="fl_unfold"')!=-1:
                pattern = re.compile(r'action-data="(\S+)"')
                fulltext_url = pattern.findall(i[2])
                fulltext_url = fulltext_url[0].replace('&amp;', '&')
                item["long"] =  'http://s.weibo.com/ajax/direct/morethan140?' + fulltext_url
                item["longpost"] =  1
            
            item["date"] =     i[3]
            item["fromDevice"]=i[4]
            item["forward"] =  i[5]
            item["comment"] =  i[6]
            item["like"] =     i[7]
            item["validate"] = i[8]
            item["mid"] = i[9]
            
            yield item   
        '''         
        for item in items:
            nickname = item.xpath('.//a/@nick-name').extract()
            mid = item.xpath('.//@mid').extract()
            nickname = nickname[0].replace('\\\\', '\\')
            nickname = nickname.replace('\\\\', '\\')
            unicode =  'u\'' + nickname + '\''
            print unicode.decode('unicode-escape')
            title.insert({'title':nickname})
        '''
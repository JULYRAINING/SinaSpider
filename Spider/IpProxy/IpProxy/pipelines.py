# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from items import ProxyItem

class IpproxyPipeline(object):
    
    
    
    def __init__(self):
        
        client = pymongo.MongoClient('localhost:27017')
        db = client['ipPool']
        self.proxy = db['proxy']
    
    def process_item(self, item, spider):
        
        if isinstance(item, ProxyItem):
            try:
                self.proxy.insert(dict(item))
            except:
                pass
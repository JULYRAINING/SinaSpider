# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class ProxyItem(scrapy.Item):
    ip = Field()
    port = Field()
    
    # define the fields for your item here like:
    # name = scrapy.Field()
    

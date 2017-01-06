# -*- coding: utf-8 -*-


BOT_NAME = 'IpProxy'

SPIDER_MODULES = ['IpProxy.spiders']
NEWSPIDER_MODULE = 'IpProxy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'IpProxy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2

DOWNLOADER_MIDDLEWARES = {
    'IpProxy.middlewares.UserAgentMiddleware': 543,
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'IpProxy.pipelines.IpproxyPipeline': 300,
}



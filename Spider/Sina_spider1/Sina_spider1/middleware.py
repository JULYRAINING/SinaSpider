# encoding=utf-8
import random

from user_agents_pc import agents
from cookies import cookies

class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookiesMiddleware(object):
    """ 换Cookie """

    def process_request(self, request, spider):
        cookie = random.choice(cookies)
        request.cookies = cookie
        
class ProxyMiddleware(object):
    
    def __init__(self):
        
        file = open('E:\Code\Git\SinaSpider\Spider\Sina_spider1\Sina_spider1\proxy_ip.txt')
        list = file.readlines()
        self.proxys = list
    
    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(self.proxys)[:-1]

        

# encoding=utf-8
import random

from cookies import cookies
from user_agents_pc import agents
import base64


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
        self.proxys = list[0].split('|')
    '''
    def process_request(self, request, spider):
        #request.meta['proxy'] = random.choice(self.proxys)[:-1]
        request.meta['proxy'] = 'http://proxy.abuyun.com:9020'
        # Use the following lines if your proxy requires authentication
        proxy_user_pass = "HL04601BMCZ51R1D:AEE87015B88EB20B"
        #setup basic authentication for the proxy
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
    '''   
    def process_request(self, request, spider):
        
        ip = random.choice(self.proxys)
        ip = 'http://'  + ip
        print('ip:' + ip)
        request.meta['proxy'] = ip
        

# encoding=utf-8
import json
import base64
import requests

"""
输入你的微博账号和密码，可去淘宝买，一元七个。
建议买几十个，微博限制的严，太频繁了会出现302转移。
或者你也可以把时间间隔调大点。
"""
'''
myWeiBo = [
    
    {'no': '13649844460', 'psw': 'q123123'},

    {'no': '13137454861', 'psw': 'q123123'},
	{'no': '13760492214', 'psw': 'q123123'},
	{'no': '13167478448', 'psw': 'q123123'},
	{'no': '13142674576', 'psw': 'q123123'},
    {'no': '15059844642', 'psw': 'q123123'},
	{'no': '18824944617', 'psw': 'q123123'},
	{'no': '13728402138', 'psw': 'q123123'},
	{'no': '15028364814', 'psw': 'q123123'},
    {'no': '18174100568', 'psw': 'q123123'},
	{'no': '18340593685', 'psw': 'q123123'},
	{'no': '15906094994', 'psw': 'q123123'},

	
]
'''
#myWeiBo = [{'no': '13649844460', 'psw': 'q123123'},]
myWeiBo = [{'no': '13261470918', 'psw': 'heaven7more'},]
def getCookies(weibo):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    #loginURL = r'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
    for elem in weibo:
        account = elem['no']
        password = elem['psw']
        username = base64.b64encode(account.encode('utf-8')).decode('utf-8')
        postData = {
            "entry": "sso",
            "gateway": "1",
            "from": "null",
            "savestate": "30",
            "useticket": "0",
            "pagerefer": "",
            "vsnf": "1",
            "su": username,
            "service": "sso",
            "sp": password,
            "sr": "1440*900",
            "encoding": "UTF-8",
            "cdult": "3",
            "domain": "sina.com.cn",
            "prelt": "0",
            "returntype": "TEXT",
        }
        session = requests.Session()
        r = session.post(loginURL, data=postData)
        jsonStr = r.content.decode('gbk')
        info = json.loads(jsonStr)
        if info["retcode"] == "0":
            print "Get Cookie Success!( Account:%s )" % account
            
            cookie = session.cookies.get_dict()
            
            cookies.append(cookie)
        else:
            print "Failed!( Reason:%s )" % info['reason']
    return cookies


cookies = getCookies(myWeiBo)
print "Get Cookies Finish!( Num:%d)" % len(cookies)

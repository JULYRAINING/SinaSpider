# encoding=utf-8
import pymongo


from items import InformationItem, TweetsItem, FollowsItem, FansItem, SearchItem


class MongoDBPipleline(object):
    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        #db = client["Sina_topic"]
        #self.Information = db["Information"]
        #self.Tweets = db["Tweets"]
        #self.Follows = db["Follows"]
        #self.Fans = db["Fans"]
        
        #db_sina_search = client["Sina_Search"]
        db_sina_search = client["Sina_Search_Guest"]
        #self.search = db_sina_search["Search"]
        self.search = db_sina_search["weibo"]
        self.Time = db_sina_search["Time"]
        
    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        
        if isinstance(item, SearchItem):
            
            for key in item:
                value = str(item[key]).replace('\\\\', '\\').replace('\\\\', '\\')
                unicode =  value
                value = unicode.decode('unicode-escape')  
                item[key] = value
            
            try:
                self.search.insert(dict(item))
                self.Time.insert({'date':item['date']})
                print 'saved'
            except Exception:
                pass
        if isinstance(item, InformationItem):
            try:
                self.Information.insert(dict(item))
            except Exception:
                pass
        elif isinstance(item, TweetsItem):
            try:
                self.Tweets.insert(dict(item))
            except Exception:
                pass
        elif isinstance(item, FollowsItem):
            followsItems = dict(item)
            follows = followsItems.pop("follows")
            for i in range(len(follows)):
                followsItems[str(i + 1)] = follows[i]
            try:
                self.Follows.insert(followsItems)
            except Exception:
                pass
        elif isinstance(item, FansItem):
            fansItems = dict(item)
            fans = fansItems.pop("fans")
            for i in range(len(fans)):
                fansItems[str(i + 1)] = fans[i]
            try:
                self.Fans.insert(fansItems)
            except Exception:
                pass
        return item

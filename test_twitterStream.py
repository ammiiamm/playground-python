import tweepy

# from this site https://wiki.morange.co.th/%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%81%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%97%E0%B8%A7%E0%B8%B4%E0%B8%95%E0%B9%80%E0%B8%95%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B8%B5%E0%B8%A1%E0%B8%A1%E0%B8%B4%E0%B9%88%E0%B8%87_API_%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B9%84%E0%B8%9E%E0%B8%98%E0%B8%AD%E0%B8%99

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

api_key = 'consumer_key'  
api_secret = 'consumer_secret'
access_token = 'token_key'
access_secret = 'token_secret'
 
class listener(StreamListener):
 
    def on_data(self, data):
        print (data)
        return True
 
    def on_error(self, status):
        print (status)
 
auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
#twitterStream = Stream(auth, listener())
#twitterStream.filter(track=["sidebyside"])


#from this site - http://tweepy.readthedocs.io/en/v2.3.0/getting_started.html#api
api =tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)

#user = tweepy.api.get_user('ammii')
#print (user.screen_name)

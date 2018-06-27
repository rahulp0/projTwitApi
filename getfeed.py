import tweepy
from tweepie import *
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(akey, asecret)
api = tweepy.API(auth)

tweets = api.home_timeline()
for tweet in tweets:
	saveFile = open('twitFeed.csv','a')
	saveFile.write(tweet.text)
	print(tweet.text)
saveFile.close()
import sys
import tweepy
import re
import time
from importlib import reload

#for encoding to the terminal window
reload(sys)


def replace_url_to_link(value):
    urls = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", re.MULTILINE|re.UNICODE)
    value = urls.sub(r'<a href="\1" target="_blank">\1</a>', value)
    
    urls = re.compile(r"([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)", re.MULTILINE|re.UNICODE)
    value = urls.sub(r'<a href="mailto:\1">\1</a>', value)
    return value

# I was taking about these-----
CONSUMER_KEY = 'oIVHi4gTLB84eTnP11FFmoIhN'
CONSUMER_SECRET = 'LUh6KoVqNqYovytM0DAMabJAM8a5lEllaCCNexBKT1HhgtinJI'
ACCESS_KEY = '1394335759-Zx6UwyAatSCrPru4N8UQQ5oIliv2B3OQDjdeh5E'
ACCESS_SECRET = 'puKymVbX1UPKPvgXzvHgVeNhWhCzMQYnXqxrxXePJGDA5'

#-----------------



tweetList = []

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
statuses = api.home_timeline()

#statuses = api.user_timeline('RahulPrksh1',count=400)


for status in statuses:
  dict={}
  dict['text'] = replace_url_to_link(status.text)
  tweetList.append(dict)
     
   

f = open("tweet.txt", "w")

for item in tweetList:
  f.write("================\n")
  f.write(item['text']+"\n")
f.close()

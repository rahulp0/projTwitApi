from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
#from tweepie import *
#import time
ckey = 'oIVHi4gTLB84eTnP11FFmoIhN'
csecret= 'LUh6KoVqNqYovytM0DAMabJAM8a5lEllaCCNexBKT1HhgtinJI'
akey = '1394335759-Zx6UwyAatSCrPru4N8UQQ5oIliv2B3OQDjdeh5E'
asecret = 'puKymVbX1UPKPvgXzvHgVeNhWhCzMQYnXqxrxXePJGDA5'
class listener(StreamListener):

	def on_data(self,data):
		print (data)
		return True
		

	def on_error(self,status):
		print("whaaaaa",status)

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(akey,asecret)

api=tweepy.API(auth)

twitterStream = Stream(auth, listener())

twitterStream.filter(track=["hey"])
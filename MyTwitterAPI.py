try:
    import json
except ImportError:
    import simplejson as json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream, ApiKeyValues

class MyTwitterAPI:
    twitter = None
    def __init__(self):
        ACCESS_TOKEN = self.access_token
        ACCESS_SECRET = self.access_secret
        CONSUMER_KEY = self.consumer_key
        CONSUMER_SECRET = self.consumer_secret
        oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        self.twitter = Twitter(auth=oauth)

    def get_tweets(self, query):
        # Search for latest tweets about "#nlproc"
        results = self.twitter.search.tweets(q='#'+query, lang='en', count=100)
        answer = ''
        for result in results["statuses"]:
            answer = answer + result['text']
        print answer
        return answer
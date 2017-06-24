from TwitterAPI import TwitterAPI
import re

def getTweets(queryString, lastId):
    tweets = []
    api = TwitterAPI(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')

    search = api.request('search/tweets', {'q':queryString, 'lang': 'en', 'count': 100, 'since_id': lastId})
    for tweet in search:
        cleanedTweet = cleanTweet(tweet['text'])
        tweets.append((tweet['id'], cleanedTweet))
    return tweets

def cleanTweet(tweet):
    removeRetweetString = re.sub('RT @.+?:\s','',tweet)
    removeUrlLink = re.sub('https?:\/\/.+?(\s|$)','',removeRetweetString)
    removeHashTags = re.sub('#.+?(\s|$)','', removeUrlLink)
    removeMentions = re.sub('@.+?(\s|$)','',removeHashTags)
    return removeMentions.rstrip()

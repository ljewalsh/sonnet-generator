from getTweets import getTweets
from countSyllables import countSyllablesInTweet
import random
import pronouncing
import time

sonnet = open('sonnet.txt', 'w')
searchTerms = ["star", "space", "rocket", "Neptune", "Jupiter", "moon",
               "planet", "astronaut", "lunar", "satellite", "alien", "spaceman"
               "orbit"]

def findTweet(lastId, searchTerm, requestNumber):
    tweets = getTweets(searchTerm, lastId)
    requestNumber = requestNumber + 1
    while len(tweets) > 0 and requestNumber < 180:
        for item in tweets:
            id, tweet = item
            lastId = id
            if countSyllablesInTweet(tweet) == 10:
                searchTerms.remove(searchTerm)
                return (id, requestNumber, tweet)
            else:
                tweets.remove(item)
    if requestNumber == 180:
        searchTerms.remove(searchTerm)
        print "sleeping for 15 minutes"
        time.sleep(900)
        return findTweet(lastId, searchTerm, requestNumber)
    else:
        return findTweet(lastId, searchTerm, requestNumber)



def getLineToRhyme(requestNumber):
    searchTerm = random.choice(searchTerms)
    id, newRequestNumber, line = findTweet('', searchTerm, requestNumber)
    return line


def getPossibleRhymes(tweet):
    wordToRhyme = getWordToRhyme(tweet)
    possibleRhymes = pronouncing.rhymes(wordToRhyme)
    return possibleRhymes

def getWordToRhyme(line):
    wordsInLine = line.split(' ')
    lastWordInLine = wordsInLine[-1]
    cleanedLastWordInLine = lastWordInLine.lower().strip(".:;?!")
    return cleanedLastWordInLine

for number in range(10):
    line = getLineToRhyme(0)
    print line
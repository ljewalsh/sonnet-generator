

def getWordsFromTweet(tweet):
    words = tweet.split(' ')
    return words

def countSyllablesInWord(word):
    vowels = "aeiouy"
    numVowels = 0
    lastWasVowel = False
    word = word.lower().strip(".:;?!")
    for wc in word:
        foundVowel = False
        for v in vowels:
            if v == wc:
                if not lastWasVowel: numVowels+=1   #don't count diphthongs
                foundVowel = lastWasVowel = True
                break
        if not foundVowel:  #If full cycle and no vowel found, set lastWasVowel to false
            lastWasVowel = False
    if len(word) > 2 and word[-2:] == "es": #Remove es - it's "usually" silent (?)
        numVowels-=1
    elif len(word) > 1 and word[-1:] == "e":    #remove silent e
        numVowels-=1
    return numVowels

def countSyllablesInTweet(TweetString):
    numberOfSyllables = 0
    wordsInTweet = getWordsFromTweet(TweetString)
    for word in wordsInTweet:
        syllablesInWord = countSyllablesInWord(word)
        numberOfSyllables += syllablesInWord
    return numberOfSyllables

# [[user@]host1:]file1 ... [[user@]host2:]file2
# file1 ... [[user@]host2:]file2

# secure copy of my file to upload

'''

scp -i MyKeyFile.pem FileToUpload.pdf ubuntu@ec2-123-123-123-123.compute-1.amazonaws.com:FileToUpload.pdf
connect to the virtual machine 
ssh -i "kimbot1.pem" ec2-user@ec2-52-201-215-131.compute-1.amazonaws.com
scp -i ~/AWS/kimbot1.pem KimBot.py ec2-user@ec2-52-201-215-131.compute-1.amazonaws.com:KimBot.py

'''

# project description
# Superhero's helping to make the drive more fun

# use @erowidrecruiter as inspiration to take phrases from kim k and mix it with einstein api or emails.
# copy similar @erowidrecruiter as pulling data from drug trip users with HR posts
# go find tweets by(WSDOT) pull responding people or and traffic condition to with superheros and food.
##################################################################################################
import tweepy
import yaml
import datetime
import random
import re
import pdb
import StateDOT
# v1    import Kim_Phrases - first ideal
# v1.1  import kim_phrases and mash with einstein quotes - started 091116
# v2    import dot traffic tweets and add superheros - launched 091216
# v3    import traffic qutoes, mesh with something kitchy cool. startup quotes change name to
        # startuptraffic. it would be localized to the city of the traffic. Change graphic to office like eroidrecruiter.
        # https://www.reddit.com/r/startups/ and a markov program with a 140 character state


# looking for a way to iterate through a list of foods from this site
# http://www.cookbooks4sale.com/recipes.php?act=alpha&char=c
# the last letter is the letter to be replaced... should this be with a %d
# so code is (link... char=%d) %d = ()

# tweet_text = origional tweet_text
# replacement_tuples = words replace
# read secret yml variables into kimbot.py
# add AWS one tweet a day to check AWS limits then go up to three to four per day.
# https://medium.com/@emckean/create-a-simple-free-text-driven-twitterbot-with-aws-lambda-node-js-b80e26209f5#.5pt271iku
##################################################################################################
def kimbot_setup():
  pass

def kimbot_auth():
  pass

def Kimbot_select():
  pass

def kimbot_tupl():
  pass

def kimbot_regx():
  pass

def kimbot_tweet():
  pass

with open("secrets.yml") as f:
    content = f.read()
# from secrets.yml import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET
secret = yaml.load(content)
##################################################################################################
# authorize tweepy with CONSUMER_KEY and CONSUMER_SECRET
auth = tweepy.OAuthHandler(secret["CONSUMER_KEY"], secret["CONSUMER_SECRET"])
auth.secure = True
# read in ACCESS_TOKEN and ACCESS_SECRET variables to tweepy
auth.set_access_token(secret["ACCESS_TOKEN"], secret["ACCESS_SECRET"])

#tweet_text = 
# Construct the API instance
API = tweepy.API(auth)
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'
##################################################################################################
#public_tweets = API.home_timeline()
#for tweet in public_tweets:
#    print tweet.text

#pulling tweets
DOTtweets = API.user_timeline("WSDOT")


# add other dot twitter accounts wsdot_traffic

#defines a function new_random_tweet, reads in twiter handle as user
def new_random_tweet(user):
    DOTtweets = API.user_timeline(user)
    tweet_text = random.choice(DOTtweets).text
    return tweet_text

tweet_text = new_random_tweet("WSDOTd")

# add list in another file of all the states that have t

        # if tweet_text contains word from replacement_tuples

# run At initialization time.
##################################################################################################

#who is responding as superhero
replacement_tuples = ( # read in first value and replace it with second
    ('police', 'Ironman'),
    ('Law Enforcement', 'Ironman'),
    ('medics', 'Hulk'),
    ('first responders', 'Blackwidow'),
    ('medivac', 'Hawkeye'),
    ('sherrif', 'Spiderman'),
    ('fire fighters', 'Captain America'),
    ('Fire Department', 'Captain America'),
    ('ambulance', 'Dr Strange'),
    ('state patrol', 'Nick Fury'),
    ('dot', 'Thor'),
    ('tow trucks', 'WarMachine'),
    ('tow truck', 'WarMachine'),

# traffic condition text swap
# find a way to add adjectives to bot
    ('accident', 'avocado'),
    ('slowdown', 'sausage'),
    ('collision', 'chimichanga'),
    ('traffic', 'tunamelt'),
    ('right lane', 'rice-noodles'),
    ('left lane', 'lambchops'),
    ('center lane', 'corn-tortilla'),
    ('one lane', 'olive-oil'),
    ('1 lane', 'olive-oil'),
    ('2 lanes', 'tomato-soup'),
    ('two lanes', 'tomato-soup'),
    ('closure', 'cranberry'),
    ('driver', 'djion-mustard'),
    ('road_rage', 'spicey-tamale'),
    ('blocked', 'blueberry'),
    ('closed', 'cornmeal'),
    ('roadway', 'corn cob'),
    ('service', 'salami'),
    ('construction', 'cashews'),
    ('delay', 'demise'),
    ('stops', 'salsa'), #added from dash tweet 10-18-16, need to find an "def element" ML? that will incorporate terms to build on its own. if replace word returns growth in tweets then keep, otherwise replace with different term.
)
##################################################################################################
# words to replace, old word with new word
replacement_words = {}
for old_word, new_word in replacement_tuples:
    old_word_regex = re.compile(old_word, re.I)
    replacement_words[old_word_regex] = new_word

tweet_has_word = False # For each tweet you want to change
while tweet_has_word == False: # when the tweet world compared to False
    for old_word_regex, new_word in replacement_words.items(): # checking for word in tweet
        if old_word_regex.search(tweet_text): # if the tweet has a word match
            tweetlist = tweet_text.split() #split it into a list      
            for word in tweetlist: # for each word
                if old_word_regex.search(word):
                    newtweet_text = tweet_text.replace(word, new_word)
            tweet_has_word = True
            #replace the word
    if tweet_has_word == False:
        tweet_text = new_random_tweet("WSDOT")

        #pdb.set_trace()
print newtweet_text
##################################################################################################
API.update_status(status=newtweet_text)

while True:
    print "This prints once a minute."
    time.sleep(60) # update the API as replacement_tuples replaces tweet_text value

# add in a 140 tweet len filter

# TODO we have a slowdown on the 405 = we have a (50(random 10,20,30,40) (weight, pound, oz, ton) chicken burrito) [monday=chicken, tuesday=beef, wednesday=pulled pork, thursday=tofu, friday=fish, saturday=salad, sunday=??????]

'''

#####
 1. Create a twitter account for your chatbot
      1a create gmail account of same name as twitterself. Tweepy

2. Pulls data off API protocols
        use keywords she uses and replace with eistein phrases
            #Mechanize vs beautiful soup
            #mech can pull data, and manage the data in form submission.

      Chat logs from the 90's
        craigslist personal adds

3. Bot ideas,
  homes for sale in certain zip completed_features
  Pull titles off buzz feed
  bot that takes Donald trump quotes and swaps Nouns, or verbs etc
    deport mexicans = import

4. Natual language toolkid
  sentiment analysis
  prounciation keystrokes
  synonym
  deep werd lynguistics stuff
  build your own corpas

# 4 read in kim tweets to a variable "kim_read_in"
    pull in tweets for 2016
        add NLP phrases processor
        minimum viable has
            pull phrase to replace from kim_phrase.py
        if tweet has ["3"] phrase
            then replace with "I'm jealous" example

# 5 replace kim tweet phrase or merge with einstein

Twitter has all sorts of bad people
  have a list of removed [do not say these words]
  have a list of words to add [replace with words from urban dictionary or insult the tweeter]

AWS has free EC2 micro instance for a year
  Digital ocean or heroku are also free minimal setup

Bot etiquette
  dont harras people
  make more amusement than annoyance
  dont avertise things
  optin not opt out
  show off with #botALLY
@lizuselton

inverse frequency - way to pick words
  use to and the as a predicate to the word
  '''
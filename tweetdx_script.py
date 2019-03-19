import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####example
# Open/Create a file to append data
csvFile = open('avii.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#example",count=100,
#replace example to your specified #hashtag
                           lang="en",
                           since="2019-03-01").items():
    print (tweet.created_at, tweet.csv)
csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

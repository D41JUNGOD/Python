import tweepy  
import datetime

consumer_key = "My consumer_key"
consumer_secret = "My consumer_secret"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

access_token = "My access_token"
access_token_secret = "My access_token_secret"
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

tweet = str(datetime.datetime.now()) + ' Brain Python Test'
api.update_status(status=tweet)

print("Successfully Posted")
print()

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

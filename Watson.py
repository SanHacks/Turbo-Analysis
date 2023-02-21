import tweepy
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, EmotionOptions
import csv
import time


# Authenticate with Twitter
auth = tweepy.OAuthHandler(SECRET_KEY, YOUR_TOKEN)
auth.set_access_token(ACCESS_TOKEN, YOUR_TWITTER_SECRET)

# Create API object
api = tweepy.API(auth)
# Authenticate with IBM Watson
authenticator = IAMAuthenticator(YOUR_KEY)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)
# Search tweets
while True:
    public_tweets = api.search_tweets("query", count=500)

    # Perform sentiment analysis on each tweet
    for tweet in public_tweets:
        response = natural_language_understanding.analyze(
            text=tweet.text,
            features=NaturalLanguageUnderstandingV1.Features(
                sentiment=NaturalLanguageUnderstandingV1.Features.SentimentOptions(document=True))).get_result()

        # Save results to CSV file
        with open("sentiment_analysis.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow([tweet.text, get_sentiment(tweet), tweet.id, tweet.created_at, tweet.retweet_count,
                             tweet.favorite_count, tweet.lang])

    # Sleep for one minute
    time.sleep(60)

import tweepy
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, EmotionOptions
import csv
import time


# Authenticate with Twitter
auth = tweepy.OAuthHandler("wnokBdU7T8LfzGujMzNwAB4MD", "KBg3A6b74pMULd6ekFr4rpQa4tKvrgTsPtN6Nk4ArMX5smuOZp")
auth.set_access_token("2393199921-aVemIxWAOOuiqTmYAlfMkwglfsGEorMFJsfJOOH", "W3S0AOPPpELwPZWfMU5Bt6T0sbEfkAe0ScOZpY1Jbt1kh")

# Create API object
api = tweepy.API(auth)
#
#{
#  "apikey": "j_9evpvoUMosyLMVc1C25PHzh-g-lytfYFu5jUcDWfQC",
#  "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:natural-language-understanding:us-south:a/16c1b95d14ce4f62ad8acf7e058d8739:fb078823-bfe8-46ef-95d1-fcea867efe13:resource-key:b849596c-1180-4b13-b569-8799e8bdbdd7",
#  "iam_apikey_name": "Auto-generated service credentials",
#  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
#  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/16c1b95d14ce4f62ad8acf7e058d8739::serviceid:ServiceId-5ebdadcf-6055-41b2-9588-c8402c1351dc",
#  "url": "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/fb078823-bfe8-46ef-95d1-fcea867efe13"
#}
# Authenticate with IBM Watson
authenticator = IAMAuthenticator('ZNzVubIo5QrXuXSD9rp1FyRYC0Xx_5mNyDEi-kR9S-TX')
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
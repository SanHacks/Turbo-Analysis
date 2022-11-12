
import tweepy
from textblob import TextBlob
import csv
import time

# Authenticate with Twitter
auth = tweepy.OAuthHandler("wnokBdU7T8LfzGujMzNwAB4MD", "KBg3A6b74pMULd6ekFr4rpQa4tKvrgTsPtN6Nk4ArMX5smuOZp")
auth.set_access_token("2393199921-aVemIxWAOOuiqTmYAlfMkwglfsGEorMFJsfJOOH", "W3S0AOPPpELwPZWfMU5Bt6T0sbEfkAe0ScOZpY1Jbt1kh")

# Create API object
api = tweepy.API(auth)

# Search tweets
while True:
    public_tweets = api.search("query", count=600)

    # Perform sentiment analysis on each tweet
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)

        # Save results to CSV file
        with open("sentiment_analysis.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow([tweet.text, analysis.sentiment, tweet.id, tweet.created_at, tweet.retweet_count, tweet.favorite_count, tweet.lang])

    # Sleep for one minute
    time.sleep(60)

    # Analyze the tweets with IBM Watson
    results = []
    for tweet in tweets:
        analysis = natural_language_understanding.analyze(
            text=tweet.text,
            features=Features(sentiment=SentimentOptions())).get_result()
        results.append({'tweet': tweet.text, 'score': analysis['sentiment']['document']['score'],
                        'label': analysis['sentiment']['document']['label']})

    # Save the results
    with open('results.json', 'w') as outfile:
        json.dump(results, outfile)
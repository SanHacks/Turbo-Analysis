import tweepy
import time
import csv
import requests
import json
from textblob import TextBlob

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def push_to_powerbi():
    pass

def get_tweets_from_search(query):
    # Authorization to consumer key and consumer secret
   # global analysis, i
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)
    #https://docs.tweepy.org/en/stable/api.html#tweepy.API.search_full_archive

    # 200 tweets to be extracted
    number_of_tweets = 200
    tweets = api.search_tweets(query, count=400)
    for tweet in tweets:
        text = tweet.text
        created_at = tweet.created_at
        retweet_count = tweet.retweet_count
        favorite_count = tweet.favorite_count
        user = tweet.user.screen_name
        tweet_id = tweet.id
        location = tweet.user.location
        #url_to_push = tweet.url
    # Empty Array
    tmp = []
    print(tmp)
    # create array of tweet information: username,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
    print(tweets_for_csv)
    for j in tweets_for_csv:
        # Appending tweets to the empty array tmp
        tmp.append(j)
    for i in tmp:
        #Get username,
    # tweet id, date/time, text
        analysis = TextBlob(i)
    #function to get the sentiment of the tweet whether it is positive or negative or neutral
        def calculate_score(tweet):
            # Calculate the polarity and subjectivity scores for the tweet
            polarity = analysis.sentiment.polarity
            subjectivity = analysis.sentiment.subjectivity

            # Assign a positive, neutral, or negative label to the tweet based on the scores
            if polarity > 0 and subjectivity > 0.5:
                return 'positive'
            elif polarity == 0:
                return 'neutral'
            else:
                return 'negative'

        def calculate_number_score(tweet):
            # Calculate the polarity and subjectivity scores for the tweet
            polaritys = analysis.sentiment.polarity
            subjectivitys = analysis.sentiment.subjectivity

            # Assign a positive, neutral, or negative label to the tweet based on the scores
            if polaritys > 0 and subjectivitys > 0.5:
                return 1  # positive
            elif polaritys == 0:
                return 0  # neutral
            else:
                return -1  # negative
        #print the sentiment of the tweet
        #write code to prit out to power bi
        print(calculate_score(i))
        print(calculate_number_score(i))
        print(analysis.sentiment)
        print(analysis.sentiment.polarity)
        print(analysis.sentiment.subjectivity)
        print(i)


    # Printing the tweets
        #Delete above code
        id_to_push = tweet_id
        user_to_push = user
        tweet_to_push = i
        sentiment_score_to_push = calculate_number_score(i)
        sentiment_to_push = calculate_score(i)
        quote_tweet_to_push = analysis.sentiment.subjectivity
        retweets_to_push = retweet_count
        likes_to_push = favorite_count
 # FORMAT JSON TO PUSH TO POWERBI
        json_data = [
            {
                "id": id_to_push,
                "user": user_to_push,
                "tweet": i,
                "sentiment": sentiment_to_push,
                "sentiment_score": sentiment_score_to_push,
                "quote_tweet": retweets_to_push,
                "replies": 0,
                "retweets": retweets_to_push,
                "likes": likes_to_push,
                "url": "AAAAA555555",
                "user_profile": 0,
                "video_views": 0,
                "video_view_quartile ": 0,
                "location": "South Africa"

            }
        ]

        res = requests.post(
            # This is the link for pushing the data with json from Twitter-Watson IBM to PowerBI(AZURE)
            # You get this link and then paste it here
            'https://api.powerbi.com/beta/1cf711ed-1eea-4b3e-95e1-4ede1a6dd023/datasets/4580cced-e587-4bd8-8563-22aa21c2c180/rows?key=V4462cc3TASydF3YXPRYHU26TAL6ET2QUDXCwhyW12Ocbk7277YcPZpEWJQqmrrwNRnh%2BRiuNkrGBhdcztvrww%3D%3D',
            data=json.dumps(json_data))
        # CODE 200 MEANS THE PUSH WAS SUCCESSFUL
        print(res.status_code)
        feedback = res.status_code

if __name__ == '__main__':
    while True:
        get_tweets_from_search('pikitup')
        print('sleeping for 5 mins')
        time.sleep(320)


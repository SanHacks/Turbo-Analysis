import tweepy
import time

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "wnokBdU7T8LfzGujMzNwAB4MD"
consumer_secret = "KBg3A6b74pMULd6ekFr4rpQa4tKvrgTsPtN6Nk4ArMX5smuOZp"
access_key = "2393199921-aVemIxWAOOuiqTmYAlfMkwglfsGEorMFJsfJOOH"
access_secret = "W3S0AOPPpELwPZWfMU5Bt6T0sbEfkAe0ScOZpY1Jbt1kh"
# Driver code
# Function to extract tweets
# Write function to get tweets form twitter search api
def get_tweets_from_search(query):
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)
#https://docs.tweepy.org/en/stable/api.html#tweepy.API.search_full_archive

    # 200 tweets to be extracted
    number_of_tweets = 200
    tweets = api.search_tweets(query, count=100)
    print(tweets)
    # Empty Array
    tmp = []

    # create array of tweet information: username,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
    for j in tweets_for_csv:
        # Appending tweets to the empty array tmp
        tmp.append(j)
    for i in tmp:
        #Get username,
    # tweet id, date/time, text
        print(i)
        print()

# Driver code
if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets_from_search("pikitup")
    time.sleep(60)


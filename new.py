import tweepy

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""
# Driver code
# Function to extract tweets
def get_tweets(username):
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)

    # 200 tweets to be extracted
    number_of_tweets = 200

    #user number of tweets
    tweets = api.user_timeline(screen_name=username)

    # Empty Array
    tmp = []

    # create array of tweet information: search,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
    for j in tweets_for_csv:
        # Appending tweets to the empty array tmp
        tmp.append(j)

    # Printing the tweets
    #format printed out tweets
    for i in tmp:
        print(i)
        print()

    print(tmp)
# Driver code
if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("ceefly_")


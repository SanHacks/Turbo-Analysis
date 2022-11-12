import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, EmotionOptions
#API Key
authenticator = IAMAuthenticator('ZNzVubIo5QrXuXSD9rp1FyRYC0Xx_5mNyDEi-kR9S-TX')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)
#URL of the service
natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/fb078823-bfe8-46ef-95d1-fcea867efe13')
# Text to analyze for emotion and sentiment
response = natural_language_understanding.analyze(
    html="<html><head><title>Fruits</title></head><body><h1>Apples and Oranges</h1><p>I love apples! I don't like oranges.</p></body></html>",
    features=Features(emotion=EmotionOptions(targets=['apples','oranges']))).get_result()
# Print the results
print(json.dumps(response, indent=2))

#Save results to CSV file
#with open("sentiment_analysis.csv", "a", newline="") as csvfile:
  # writer = csv.writer(csvfile, delimiter=",")
  #  writer.writerow([tweet.text, get_sentiment(tweet), tweet.id, tweet.created_at, tweet.retweet_count,
     #                tweet.favorite_count, tweet.lang])


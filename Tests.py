import requests
import time
import json

json_data =[
    {
"id": 98.6,
"user": "Gundo",
"tweet": "AAAAAA",
"sentiment": "Sad",
"sentiment_score": 98.6,
"quote_tweet": "AAAAA555555",
"replies": 98.6,
"retweets": 98.6,
"likes": 98.6,
"url": "AAAAA555555",
"user_profile": "AAAAA555555",
"video_views": "AAAAA555555",
"video_view_quartile ": "AAAAA555555",
"location": "AAAAA555555"

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

if res.status_code == 200:
    print("UPDATE SUCCESSFUL")
#print(json_data)
print('Just gonna rest for a while')
if res.status_code == 400:
    print("Pushing to powerBI failed!")
    time.sleep(60)

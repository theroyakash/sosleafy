import tweepy
import os
import requests
import random

API_KEY = os.environ["API_KEY"]
API_SECRET_KEY = os.environ["API_SECRET_KEY"]

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
SECRET_ACCESS_TOKEN = os.environ["SECRET_ACCESS_TOKEN"]

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_ACCESS_TOKEN)
api = tweepy.API(auth)

import time
random.seed(time.time())

def tweet():
    india_news = 'https://raw.githubusercontent.com/theroyakash/newsapis/main/india_news.json'
    us_news = 'https://raw.githubusercontent.com/theroyakash/newsapis/main/us_news.json'

    india_content = requests.get(india_news).json()
    us_content = requests.get(us_news).json()


    india_articles = india_content["articles"]
    us_articles = us_content["articles"]

    us_randomarticle = random.choice(us_articles)
    us_title = us_randomarticle["title"]
    us_url = us_randomarticle["url"]

    india_randomarticle = random.choice(india_articles)
    india_title = india_randomarticle["title"]
    india_url = india_randomarticle["url"]

    api.update_status(f"{india_title} is available here: {india_url}")
    api.update_status(f"{us_title} is available here: {us_url}")

if __name__ == "__main__":
    try:
        tweet()
    except:
        print("Error Running the program")
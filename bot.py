import tweepy
import apiauth
import requests
import random

API_KEY = apiauth.API_KEY
API_SECRET_KEY = apiauth.API_SECRET_KEY

ACCESS_TOKEN = apiauth.ACCESS_TOKEN
SECRET_ACCESS_TOKEN = apiauth.SECRET_ACCESS_TOKEN

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_ACCESS_TOKEN)
api = tweepy.API(auth)

india_news = 'https://raw.githubusercontent.com/theroyakash/newsapis/main/india_news.json'
content = requests.get(india_news).json()

articles = content["articles"]

randomarticle = random.choice(articles)
title = randomarticle["title"]
url = randomarticle["url"]

api.update_status(f"{title} is available here: {url}")

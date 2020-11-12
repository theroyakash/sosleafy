import tweepy
import apiauth

API_KEY = apiauth.API_KEY
API_SECRET_KEY = apiauth.API_SECRET_KEY

ACCESS_TOKEN = apiauth.ACCESS_TOKEN
SECRET_ACCESS_TOKEN = apiauth.SECRET_ACCESS_TOKEN

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_ACCESS_TOKEN)
api = tweepy.API(auth)

api.update_status("TEST")

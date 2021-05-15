from github import Github, InputGitAuthor
import requests
import json
import base64

token = "f932b7dfcb0a92c1f81c0da1f2b00d2d83740b4a"
g = Github(token)

india_content = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=b2f4af4118684eeaa6b9b0db99fc98d5').json()
india_content = json.dumps(india_content)

us_content = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=b2f4af4118684eeaa6b9b0db99fc98d5').json()
us_content = json.dumps(us_content)

uk_content = requests.get('https://newsapi.org/v2/top-headlines?country=gb&apiKey=b2f4af4118684eeaa6b9b0db99fc98d5').json()
uk_content = json.dumps(uk_content)

repo = g.get_repo("theroyakash/newsapis")

indiafile = repo.get_contents("india_news.json")
usfile = repo.get_contents("us_news.json")
ukfile = repo.get_contents("uk_news.json")

# update
repo.update_file(indiafile.path, "JSON Updated for India", india_content, indiafile.sha)
repo.update_file(usfile.path, "JSON Updated for United states", us_content, usfile.sha)
repo.update_file(ukfile.path, "JSON Updated for United Kingdom", uk_content, ukfile.sha)

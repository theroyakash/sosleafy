import requests
import random


india_news = 'https://raw.githubusercontent.com/theroyakash/newsapis/main/india_news.json'

india_content = requests.get(india_news).json()
india_articles = india_content["articles"]


india_randomarticle = random.choice(india_articles)
india_title = india_randomarticle["title"]
india_url = india_randomarticle["url"]
sources = india_randomarticle["source"]['name']

india_content = india_randomarticle["content"][:-12] if india_randomarticle["content"] !=None else ""



botAPIendPoint = f"https://api.telegram.org/bot1526002772:AAHfkowpexvNEFAna6elfdGAHrEPdY3fZA8/sendMessage?chat_id=-1001236049850"

if __name__ == "__main__":

    requests.get(botAPIendPoint, params={'parse_mode': 'markdown', 'text': f"*{india_title}* \n\nBy *{sources}* \n\n{india_content} \n[See Article]({india_url})"})
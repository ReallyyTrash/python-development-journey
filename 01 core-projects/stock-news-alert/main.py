import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

# Load environment variables from .env file
load_dotenv()

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
to_number = os.getenv("TWILIO_TO_NUMBER")
from_number = os.getenv("TWILIO_FROM_NUMBER")

stock_para = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

news_endpoint = "https://newsapi.org/v2/everything"
news_para = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
    "sortBy": "popularity",
    "language": "en",
}

emoji = None
decreasing_emoji = "🔻"
increasing_amojij = "🔺"    

def send_message(i):
    global news_title, news_article, news_desc, account_sid
    news_title = news_title[i]
    news_desc = news_desc[i]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body=f"{news_article}",
    )

stock_response = requests.get(STOCK_ENDPOINT, stock_para)

news_response = requests.get(news_endpoint, news_para)

news_data = news_response.json()['articles'][:3]
news_title = [a['title'] for a in news_data]
news_desc = [a['description'] for a in news_data]
news_article = f"Headline: {news_title} \nBrief: {news_desc}"



for i in range(3):
    send_message(i)

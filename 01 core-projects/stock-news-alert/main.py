import requests, os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "N6M7G6BJY31ZI5X3"
stock_para = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

news_endpoint = "https://newsapi.org/v2/everything"
news_apikey = "a29009430f3641e18dc2287dcf6b6cee"
news_para = {
    "apiKey":  news_apikey,
    "qInTitle": COMPANY_NAME,
    "sortBy": "popularity",
    "language": "en",
}

account_sid = "AC50045f59fab9aa7b861951889d2f940b"
auth_token = '787be373797e2f134d76b0054263df07'

emoji = None
decreasing_emoji = "🔻"
increasing_amojij = "🔺"

def send_message(i):
    global news_title,news_article, news_desc, account_sid
    news_title = news_title[i]
    news_desc = news_desc[i]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to= "+916350015420",
        from_= '+12294583349',
        body=f"{news_article}",
    )

stock_response = requests.get(STOCK_ENDPOINT, stock_para)

# stock_data = stock_response.json()['Time Series (Daily)']
# print(stock_data)
# data_list = [value for (key, value) in stock_data.items()]
#
# yesterday_stock = float(data_list[0]["4. close"])
# day_before_yes_stock = float(data_list[1]["4. close"])
#
# stock_difference = (yesterday_stock - day_before_yes_stock)/yesterday_stock*100

## Setting the emoji for texting
# if abs(stock_difference) > 0:
#     emoji = increasing_amojij
# else:
#     emoji = decreasing_emoji



# print(message.status)


news_response = requests.get(news_endpoint, news_para)

news_data = news_response.json()['articles'][:3]
news_title = [a['title'] for a in news_data]
news_desc = [a['description'] for a in news_data]
news_article = f"Headline: {news_title} \nBrief: {news_desc}"



for i in range(3):
    send_message(i)
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

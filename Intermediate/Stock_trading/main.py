import requests
import smtplib

from Private_keys import MY_EMAIL, MY_PASSWORD,STOCK_API_KEY,NEWS_API_KEY

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

news_parameter = {
    "q": COMPANY_NAME,
    "apikey" : NEWS_API_KEY
}

response = requests.get(STOCK_ENDPOINT,params=stock_parameters)
print(response.raise_for_status())
data = response.json()
print(data)
time_series  = data["Time Series (Daily)"]

data_list = [value for key,value in time_series.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)


day_before_closing_prices = data_list[1]["4. close"]
print(day_before_closing_prices)

positive_differences = (float(yesterday_closing_price)- float(day_before_closing_prices))
print(positive_differences)

if positive_differences > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

pd = round(positive_differences / float(day_before_closing_prices))*100
print(pd)

if abs(pd )> 0.2:
    news_response = requests.get(NEWS_ENDPOINT,params=news_parameter)
    articles = news_response.json()["articles"]

three_articles = articles[:3]
print(three_articles)

formatted_article = [f"{STOCK_NAME}: {up_down}{pd}%\nHeadline:{article['title']}, \nBrief: {article['description']}" for article in three_articles]


for article in formatted_article:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL,password = MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="airdrop.email00@gmail.com",
            msg=article
        )

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

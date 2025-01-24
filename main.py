#top 3 news about the stock about a paricular company and stock...
import requests
from twilio.rest import Client
stock_name="TESLA"
company_name="Tesla Inc"
stock_endpoint="https://www.alphavantage.co/query"
news_endpoint="https://newsapi.org/v2/everything"
stock_api_key="85PPYPARXVKLP1M0"
news_api="1b626842b7ab4b36ab38a43c68b7a5ee"
twilio_sid="ACe4dda6f37d1f6afa7e78036cd416b5ea"
twilio_auth_token="33776b401644d42b3631320697319c65"
 
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":stock_name,
    "apikey":stock_api_key,
} 
response=requests.get(stock_endpoint, params=stock_params)
data=response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
print(yesterday_closing_price)
day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)
difference=float(yesterday_closing_price)-float(day_before_yesterday_closing_price)
up_down=None
if difference>0:
    up_down="▲"
else:
    up_down="▼"
print("difference:"+str(difference))
difference_percentage=round((difference/float(yesterday_closing_price))*100)
print("percentage_difference:"+str(difference_percentage))

num_to_message ='+917981259825'

if abs(difference_percentage) >1:
    news_params={
        "apiKey": news_api,
        "qInTitle": company_name,
    }
    news_response=requests.get(news_endpoint, params=news_params)
    articles=news_response.json()["articles"]
    print(articles)
    three_articles=articles[:3]
    print(three_articles)
    formatted_article=[f"{stock_name}:{up_down}{difference_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}"for article in three_articles]
    client=Client(twilio_sid, twilio_auth_token)
    for article in formatted_article:
        
        message=client.messages.create(
            body=article,
            from_="+13347218081",
            to=num_to_message
            )
 
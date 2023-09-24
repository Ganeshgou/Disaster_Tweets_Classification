import tweepy
import csv
import datetime

consumer_key = 'mUCZmSwuGjKT5KAChoUaCpgMm'
consumer_secret = 'aEH14EfhAvzzrXP5k6U1Twq3xv30ByH5WY6WC3MHWRPYA'
access_token = 'your_access_token_here'
access_token_secret = 'your_access_token_secret_here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

start_date_str = input("Enter start date (yyyy-mm-dd): ")
end_date_str = input("Enter end date (yyyy-mm-dd): ")
query = input("Enter search query: ")


start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')

tweets = tweepy.Cursor(api.search_tweets, q=query, lang='en', tweet_mode='extended').items()

with open('tweets.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["date", "username", "text"])
    
    for tweet in tweets:
        if start_date <= tweet.created_at <= end_date:
            writer.writerow([tweet.created_at, tweet.user.name, tweet.full_text])
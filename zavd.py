import tweepy
from textblob import TextBlob

# Авторизація Twitter API
api_key = "ВАШ_API_KEY"
api_key_secret = "ВАШ_API_KEY_SECRET"
access_token = "ВАШ_ACCESS_TOKEN"
access_token_secret = "ВАШ_ACCESS_TOKEN_SECRET"

# Встановлення з'єднання
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Збір твітів
hashtag = "#example"
tweets = tweepy.Cursor(api.search_tweets, q=hashtag, lang="en").items(100)

# Аналіз тональності
positive, neutral, negative = 0, 0, 0

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
        positive += 1
    elif analysis.sentiment.polarity == 0:
        neutral += 1
    else:
        negative += 1

# Виведення результатів
total = positive + neutral + negative
if total > 0:
    print(f"Positive: {100 * positive / total:.2f}%")
    print(f"Neutral: {100 * neutral / total:.2f}%")
    print(f"Negative: {100 * negative / total:.2f}%")
else:
    print("No tweets found.")

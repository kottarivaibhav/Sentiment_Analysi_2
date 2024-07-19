import csv
import random
from datetime import datetime, timedelta

# Sample data for mobile phone features tweets with sentiments
positive_tweets = [
    "The battery life of this phone is amazing! Lasts all day.",
    "The display is so vibrant and clear, absolutely love it!",
    "Loving the new software update, everything runs smoother.",
    "The camera quality on the {} is amazing.",
    "Really happy with the performance of my new {}.",
    "The {} is really sleek and fast.",
    "The {} has exceeded my expectations!",
    "Battery life on the {} is excellent.",
    "My {} runs all my apps smoothly.",
    "I'm impressed with the build quality of the {}.",
    "The {} is a great value for the price."
]
neutral_tweets = [
    "The camera quality is decent, but could be better.",
    "It's a good phone, but the speaker isn't very loud.",
    "Battery life on the {} could be better.",
    "Having some issues with my {}. Anyone else?",
    "Not too impressed with the {}. Expected more.",
    "Touchscreen on my {} is unresponsive at times.",
    "My {} is slower than expected.",
    "Experiencing connectivity issues with the {}.",
    "The camera on the {} is decent.",
    "The display on the {} is okay."
]
negative_tweets = [
    "I hate how slow the phone gets after a few months.",
    "The phone's build quality feels cheap and fragile.",
    "The phone heats up too quickly during gaming sessions.",
    "Why is my {} overheating?",
    "The {} keeps crashing. Frustrated!",
    "Touchscreen on my {} is unresponsive at times.",
    "My {} is slower than expected.",
    "Experiencing connectivity issues with the {}.",
    "The camera on the {} is disappointing.",
    "I regret buying the {}. Not worth the money."
]

# Combine positive, neutral, and negative tweets
all_positive_tweets = random.choices(positive_tweets, k=1000)
all_neutral_tweets = random.choices(neutral_tweets, k=1000)
all_negative_tweets = random.choices(negative_tweets, k=1000)

all_tweets = (
    [(tweet, "positive") for tweet in all_positive_tweets] +
    [(tweet, "neutral") for tweet in all_neutral_tweets] +
    [(tweet, "negative") for tweet in all_negative_tweets]
)

# Shuffle the tweets to mix them
random.shuffle(all_tweets)

# Generate random date
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

# Define date range
start_date = datetime(2016, 7, 1)
end_date = datetime(2016, 9, 30)

# Generate CSV data for mobile phone products
mobile_phones = ['iPhone', 'Samsung Galaxy', 'Google Pixel', 'OnePlus', 'Xiaomi']
mobile_rows = []
for tweet, sentiment in all_tweets:
    product = random.choice(mobile_phones)
    date_time = random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')
    mobile_rows.append([product, tweet, date_time, sentiment])

# Write to CSV file
with open('mobile_phone_tweets_balanced.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['product', 'content', 'date_time', 'sentiment'])
    writer.writerows(mobile_rows)

print("CSV file 'mobile_phone_tweets_balanced.csv' has been created.")

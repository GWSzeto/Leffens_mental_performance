import tweepy 
from pprint import pprint
import time

consumer_key = 'itLJwqsB1ipm7IHeNg9dtUbzg'
consumer_secret = 'HGV0cawZcvgsiFqngzx0ImRdbJcVQz9j1po9X5gWN7WEIW9cFB'
access_key = '2869971100-QtnvCMYAbziLK9sY5iakKLu4iWAxAB5Ep2fRUlE'
access_secret = 'CpEmXS17hq0hBNaKNH1pAAj8GZasSUeIlGCpUwKreUZYG'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

query = api.search_users(q='doublelift')
leffen_id = query[0].screen_name
print leffen_id
print query[0].created_at
stat = api.user_timeline(screen_name='TSMDoublelift', max_id='658042037028020224')
for s in stat:
    print s.text
    print s.created_at
    print s.id
    print

# print stat.created_at
# print stat.text

# for tweet in api.user_timeline(id=leffen_id):
#     print tweet.text
#     print tweet.created_at
#     print ""
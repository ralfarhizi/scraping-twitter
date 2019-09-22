# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 19:48:47 2019

@author: Bang In
"""

import tweepy as tw
import pandas as pd
import csv
import unicodedata

#Twitter API credentials
consumer_key = "yArlrrMDUtThJae0GOxYsXyrQ"
consumer_secret = "oSEflOfqQygAsYDPTgzkymdWoCxpxZMuTTOQBjIKAgnRzRYVJw"
access_token = "158666437-h29COCbYv9u7XWnucpfbbcLQ0hiVkSGPaeIKLwdO"
access_token_secret = "MqVMByRZ7PlhqzwLOUq3nbBIcXScq18VsuhyqEXkWezxC"

def get_all_tweets(search_words):
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    
    # Post a tweet from Python
    #api.update_status("Look, I'm tweeting from #Python in my #earthanalytics class! @EarthLabCU")
    # Your tweet has been posted!
    
    date_since = "2019-01-01"
    
    # To Keep or Remove Retweets
    new_search = search_words + " -filter:retweets"
    
    # New Search to get information about whos tweeting and their loc
    tweets = tw.Cursor(api.search,
                       tweet_mode='extended',                       
                       q=new_search,
#                       lang="en",
                       since=date_since).items(100)
    
    all_tweets = [[tweet.id_str, tweet.created_at, tweet.user.screen_name, unicodedata.normalize('NFKD', tweet.full_text).encode('ascii','ignore'), unicodedata.normalize('NFKD', tweet.user.location).encode('ascii','ignore')] for tweet in tweets]
#    print(all_tweets[:100])

    tweet_text = pd.DataFrame(data=all_tweets, 
                    columns=['tweet_id', 'timestamp', 'user', 'tweet', 'location'])
    print(tweet_text)
    #write the csv	
    with open('%s_tweets.csv' % search_words, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['tweet_id', 'timestamp', 'user', 'tweet', 'location'])
        writer.writerows(all_tweets)

    pass


if __name__ == '__main__':
    get_all_tweets("RKUHP")
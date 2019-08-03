"""
PostivityPingBot v1.0 by Minhduc Cao - 2019.07.30
Randomly replies to Reddit comments with a positive message daily
"""
import praw
import credentials

reddit = praw.Reddit(user_agent='PositivityPingBot v1.0',
                     username=credentials.username,
                     password=credentials.password,
                     client_id=credentials.client_id,
                     client_secret=credentials.client_secret)
#print(reddit.user.me())

subreddit = reddit.subreddit('cardistryredesign')

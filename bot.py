"""
PostivityPingBot v1.0 by Minhduc Cao - 2019.08.06
Randomly replies to Reddit comments with a positive message daily
"""
import praw
import time
import random

FILTER_SUGGESTIONS = False      # Set to True to vet suggested reply messages, currently unused
DELAY = 86400                   # Currently set to reply every 24 hours (in seconds)


def setup():
    """Creates Reddit instance for the bot"""
    print("Starting authentication...")
    reddit = praw.Reddit('PositivityPingBot')
    print("Authenticated bot:", str(reddit.user.me()))
    return reddit


def load_messages():
    """Loads text file containing reply messages"""
    with open('messages.txt', 'r') as messages:
        messageList = []
        for line in messages:
            # Adds explanatory line for each reply message
            messageList.append(line.strip() + "\n*****\n^(This comment was made by a bot! PM me if you would like to suggest a positive message (:)")
    return messageList


def run_bot(reddit, messages, last_reply_time):
    """Runs PositivityPingBot, checks PMs for suggestions and replies to a random comment daily"""
    for pm in reddit.inbox.unread(limit=None):
        userMention = pm.subject == 'username mention'
        userReply = pm.subject == 'comment reply'

        # Ignore inbox messages that are username mentions or comment replies
        if not (userMention or userReply):
            with open('suggestions.txt', 'a') as suggestions:
                print('Adding suggestion: {}'.format(pm.body))
                suggestions.write(pm.body + '\n')
        reddit.inbox.mark_read([pm])                                    # Marks PM as read

    # Runs if it's time to post a daily reply
    if time.time() - last_reply_time >= DELAY:
        results = reddit.subreddit('cardistryredesign').comments()      # Using r/cardistryredesign as a test
        comments = {result.id: result for result in results}            # Stores comment ID and Reddit comment obj into a dict

        # Checks if no comments can be found
        if len(comments) == 0:
            print('Error: No comments found.')
        else:
            randomID = random.choice(list(comments.keys()))
            print('Replied to comment: {}'.format(randomID))
            comments[randomID].reply(random.choice(messages))
            return time.time()
    time.sleep(60)
    return last_reply_time


if __name__ == '__main__':
    messages = load_messages()
    reddit = setup()
    last_reply_time = time.time() - DELAY                              # - DELAY is to start posting
    while True:
        last_reply_time = run_bot(reddit, messages, last_reply_time)
        print(last_reply_time)

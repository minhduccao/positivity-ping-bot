"""
PostivityPingBot v1.0 by Minhduc Cao - 2019.08.06
Randomly replies to Reddit comments with a positive message daily
"""
import praw
import time
import random


def setup():
    """Creates Reddit instance for the bot"""
    print("Starting authentication...")
    reddit = praw.Reddit('PositivityPingBot')
    print("Authenticated bot:", str(reddit.user.me()))
    return reddit


def loadMessages():
    with open('messages.txt') as messages:
        messageList = []
        for line in messages:
            messageList.append(line.strip())
    return messageList

def runBot(reddit, oldCommentID, messages):
    """Runs PositivityPingBot and returns old comment ID"""
    results = reddit.subreddit('cardistryredesign').comments()      # Using r/cardistryredesign as a test
    comments = {result.id: result for result in results}       # Stores comment ID and Reddit comment obj into a dict
    valid = True

    while valid:
        # Checks if no comments can be found
        if len(comments) == 0:
            print('Error: No comments found.')
            break

        # Checks if previous bot reply was the same comment
        randomID = random.choice(list(comments.keys()))
        if randomID == oldCommentID:
            print('Error: Replying to same comment.')
            break

        print('Replied to comment: {}'.format(randomID))
        comments[randomID].reply(random.choice(messages))
        oldCommentID = randomID
        break
    return oldCommentID


if __name__ == '__main__':
    oldCommentID = ''
    messages = loadMessages()
    reddit = setup()
    while True:
        oldCommentID = runBot(reddit, oldCommentID, messages)
        time.sleep(60)

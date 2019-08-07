# PositivityPingBot
This Reddit bot will reply to a random user's comment with a positive message every 24 hours and allow users to suggest messages through PMs.

This bot extracts the most recent 100 comments from r/all (Reddit's frontpage) every 24 hours and chooses 1 out of the 100 comments to reply to with a positive message. The bot also accepts suggestions through private messages and allows the user to vet suggestions to be added to a list of potential replies.

---
# Usage
```
1. Clone repository
2. Download and install PRAW
3. Add in Reddit credentials into praw.ini
4. Run bot.py
5. (OPTIONAL) Add custom messages into 'messages.txt'
6. (OPTIONAL) Set 'FILTER SUGGESTIONS' to True to vet suggested messages upon start
7. (OPTIONAL) Set 'DELAY' to your suggested 
```

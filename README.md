# TwitterBot
## Description
Bot that tweets a status and image once a day from the top postings of a subreddit.
## Set Up
First you'll need a [Twitter developer account][twitDevLink].
1. Sign in with a Twitter account
2. Create a new app
3. Modify the settings of the app to allow read & write
4. Generate necessary OAuth tokens

Either hardcode credentials in config.py or add environment variables with credentials.

You'll also need a reddit account to use reddit API. Go to preferences in [reddit][redditDevLink].

You can install the tweepy library with:

    pip install tweepy

You can install the reddit library with:

    pip install praw

Change SUBREDDIT variable in main to whatever subreddit you choose

Change the wait time to whatever frequency you would like, and look into [praw API][prawLink] 
for other cool things you can do with the API.

[twitDevLink]: https://developer.twitter.com/en
[redditDevLink]: https://www.reddit.com/prefs/apps
[prawLink]: https://praw.readthedocs.io/en/latest/
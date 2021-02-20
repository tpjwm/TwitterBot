import tweepy
import logging
from config import create_api
from config import reddit_api
import requests
import os
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

SUBREDDIT = "comedyheaven"


# Automatically follow followers
def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()


# Tweets text with media object
def tweet(text, media, api):
    api.update_status(text, media_ids=[media.media_id])
    logger.info("Tweeting...")


# Gets a media object from reddit image url
def get_media(url, api):
    filename = 'temp.png'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        media = api.media_upload(filename)
        os.remove(filename)
        return media
    else:
        print("Unable to download image")


def main():
    api = create_api()
    reddit_app = reddit_api()

    while True:
        # Posts top tweet of the day from SUBREDDIT
        for submission in reddit_app.subreddit(SUBREDDIT).top("day", limit=1):
            tweet_text = submission.title
            url = submission.url
            tweet(tweet_text, get_media(url, api), api)

        follow_followers(api)

        logger.info("Waiting...")

        time.sleep(86400)


if __name__ == "__main__":
    main()

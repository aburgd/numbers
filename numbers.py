from gtts import gTTS
from os import urandom
from sys import byteorder
from time import sleep
import tweepy
import settings


cons_key = settings.CONSUMER_KEY
cons_sec = settings.CONSUMER_SECRET
acc_key = settings.ACCESS_KEY
acc_sec = settings.ACCESS_SECRET


def tweepy_setup(cons_key, cons_sec, acc_key, acc_sec):
    auth = tweepy.OAuthHandler(cons_key, cons_sec)
    auth.set_access_token(acc_key, acc_sec)
    api = tweepy.API(auth)
    return api


def big_number():
    num_l = []
    for i in range(1, 5):
        n_bytes = urandom(8)
        num = int.from_bytes(n_bytes, byteorder)
        num_l.insert(0, str(num))
    return "".join(num_l)


def tweet(api, tweet):
    api.update_status(tweet)
    sleep(86400)

try:
    print("Running")
    tweepy_setup(cons_key, cons_sec, acc_key, acc_sec)
    number = big_number()
    tweet(api, number)
except KeyboardInterrupt:
    print("WARN - Stopping")

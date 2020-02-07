#!/usr/bin/python3
"""
Returns number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    subreds = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    red_req = requests.get(subreds, headers={'User-Agent': 'lee'})
    if (red_req.status_code == requests.codes.ok):
        jason_full = red_req.json()
        return(jason_full['data']['subscribers'])
    else:
        return (0)

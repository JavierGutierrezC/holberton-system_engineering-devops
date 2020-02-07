#!/usr/bin/python3
import requests


def top_ten(subreddit):
    subred = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    red_req = requests.get(subred, headers={'User-Agent': 'h'})
    if (red_req.status_code == requests.codes.ok):
        jason_red = red_req.json()
        for i in range(len(jason_red['data']['children'])):
            print(jason_red['data']['children'][i]['data']['title'])
    else:
        print(None)

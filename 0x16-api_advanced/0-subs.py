#!/usr/bin/python3
"""function that queries the Reddit API and returns the
number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the
    number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=user_agent)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0

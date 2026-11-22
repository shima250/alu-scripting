#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get('data')
    if data is None:
        print(None)
        return
    for child in data.get('children', [])[:10]:
        print(child.get('data').get('title'))

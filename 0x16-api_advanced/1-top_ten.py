#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Fetches and prints the titles of the first 10 hot posts for given subreddit

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    headers = {'User-Agent': 'MyBot/0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
    else:
        print(None)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

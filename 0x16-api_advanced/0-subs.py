#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
of a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers for the subreddit or 0 if the subreddit
    is invalid.
    """
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    else:
        return 0

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
        ubreddit (str): The name of the subreddit.

    Returns:
        nt: The number of subscribers for the subreddit or 0 if the subreddit
    is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Chrome/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

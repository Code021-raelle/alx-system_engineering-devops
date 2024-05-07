#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing the titles
of a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit
        hot_list (list): A list to store the titles of hot articles
        after (str): The parameter used for pagination.

    Returns:
        list or None: A list containing the titles of all hot articles
        for the subreddit
    """
    headers = {'User-Agent': 'MyBot/0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    response = response.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        if children:
            for child in children:
                hot_list.append(child['data']['title'])
            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")

#!/usr/bin/python3
"""
This module prints sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, counts={}, after=""):
    """
        Recursive function to query Reddit API for given subreddit
        Prints sorted count of given keywords
    """
    url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
    if after:
        url = "{}&after={}".format(url, after)
    headers = {'User-Agent': 'CustomClient/1.0'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        print_counts(counts)
        return
    r = r.json()
    if 'data' in r:
        data = r.get('data')
        if not data.get('children'):
            return hot_list
        for post in data.get('children'):
            for word in post.get('data').get('title').lower().split():
                if word in word_list:
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1
        if not data.get('after'):
            print_counts(counts)
        else:
            count_words(subreddit, word_list, counts, data.get('after'))
    else:
        print_counts(counts)


def print_counts(counts):
    """
        Sort and print values in counts
    """
    if not counts:
        return
    rev_counts = {}
    for key, value in counts.items():
        rev_counts[value] = key
    for key in sorted(rev_counts, reverse=True):
        print("{}: {:d}".format(rev_counts[key], key))

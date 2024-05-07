#!/usr/bin/python3
"""
Queries the Reddit API recursively, parses the title of all hot articles
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles
    and prints a sorted count of a given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): The parameter used for pagination.
        count_dict (dict): A dicitonary to store the counts of keywords.

    Returns:
        None
    """
    if count_dict is None:
        count_dict = {}

    headers = {'User-Agent': 'MyBot/0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        if children:
            for child in children:
                title = child['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        count_dict[word.lower()] = count_dict.get(
                                word.lower(), 0) + title.count(word.lower())
            after = data['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, after, count_dict)
            else:
                sorted_counts = sorted(
                        count_dict.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            print(None)
    else:
        print(None)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(
            sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2].split())

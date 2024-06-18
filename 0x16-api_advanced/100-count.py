#!/usr/bin/python3
"""A function that queries the Reddit API recursively."""

import requests


def count_words(subreddit, keywords, after='', word_counts={}):
    """
    Recursively queries the Reddit API, parses the titles of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces; e.g., "JavaScript"
    If no posts match or the subreddit is invalid, it prints nothing.

    Args:
        subreddit (str): The name of the subreddit to query.
        keywords (list): A list of keywords to count in post titles.
        after (str): A token for pagination (default is an empty string).
        word_counts (dict): A dictionary to store the counts of keywords.

    Returns:
        None
    """
    if not word_counts:
        for keyword in keywords:
            if keyword.lower() not in word_counts:
                word_counts[keyword.lower()] = 0

    if after is None:
        sorted_word = sorted(word_counts.items(), key=lambda x: (-x[1], x[0])
                             )
        for keyword, count in sorted_word:
            if count:
                print('{}: {}'.format(keyword, count))
        return None

    u = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}

    r = requests.get(u,
                     headers=headers,
                     params=parameters,
                     allow_redirects=False)

    if r.status_code != 200:
        return None

    try:
        posts = r.json()['data']['children']
        after_token = r.json()['data']['after']
        for post in posts:
            title = post['data']['title']
            title_words = [word.lower() for word in title.split(' ')]

            for keyword in word_counts.keys():
                word_counts[keyword] += title_words.count(keyword)

    except Exception:
        return None

    count_words(subreddit, keywords, after_token, word_counts)

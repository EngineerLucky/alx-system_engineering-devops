#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves a list of titles of hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to fetch posts from.
        hot_list (list): A list to store the post titles.
        after (str): A token to paginate through posts.
        count (int): The total count of posts processed (default is 0).

    Returns:
        list: A list of post titles from the subreddit.
    """
    b = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user_agent = "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    headers = {"User-Agent": user_agent}
    params = {"after": after, "count": count, "limit": 100}

    r = requests.get(b, headers=headers, params=params, allow_redirects=False)

    if r.status_code == 404:
        return None

    results = r.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list

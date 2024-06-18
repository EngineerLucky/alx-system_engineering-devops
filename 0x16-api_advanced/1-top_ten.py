#!/usr/bin/python3
"""this module contains the function top_ten"""


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the top 10 hot post.

    Args:
        subreddit (str): The name of the subreddit to fetch hot posts from.
    """
    import requests

    # Construct the URL to request the top 10 hot posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Set custom headers for the request
    headers = {"User-Agent": "My-User-Agent"}

    # Send a GET request to the Reddit API's subreddit's hot posts endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the HTTP status code indicates an error (status code >= 300)
    if response.status_code >= 300:
        print('None')
    else:
        # Extract and print the titles of the top 10 hot posts
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))

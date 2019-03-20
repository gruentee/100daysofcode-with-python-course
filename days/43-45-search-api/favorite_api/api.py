import requests
from collections import namedtuple
from typing import List

BASE_URL = "http://search.talkpython.fm/api/search"

Episode = namedtuple("Episode", "category,id,url,title,description")


def search(query: str) -> List[Episode]:
    """Query TalkPython API

    :parameter query: the search term
    :returns: a list of Episodeds"""
    results = requests.get(BASE_URL, params={"q": query})
    results.raise_for_status()

    if len(results.text):
        episodes = [Episode(**e) for e in results.json().get('results')]
    else:
        episodes = []
    return episodes

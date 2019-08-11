import urllib.parse

import requests
from bs4 import BeautifulSoup as bs

import episode


class Podcast:
    class Qualifiers:
        episode = ['a', {'class', 'archive-post-title'}]

    def __init__(self, url=None):
        self.url = None

        self.episodes = []
        self.artists = []

        if url:
            self.load(url)

    def load(self, url=None):
        if url:
            self.url = url

        page = requests.get(url)
        soup = bs(page.text, 'html.parser')

        nodes = soup.find_all(*self.Qualifiers.episode)
        for node in nodes:
            url = node.get('href')
            abs_url = urllib.parse.urljoin(self.url, url)
            e = episode.Episode(self, abs_url)
            self.episodes.append(e)
            e.parse_tracks()

import logging

import dateutil.parser
import requests
from bs4 import BeautifulSoup as bs


class Episode:
    class Qualifiers:
        song = ['span', {'class': 'toc-text'}]
        id = ['a', {'class': 'volume-link'}]
        title = ['h1', {'class': 'post-title'}]
        date = ['time', {'itemprop': 'datePublished'}]

    def __init__(self, url=None):
        self.url = None

        self.id = None
        self.title = None
        self.date = None

        self.raw_tracks = []
        self.tracks = []

        if url:
            self.load(url)

    def __repr__(self):
        return (
            f'<{self.__class__.__name__} '
            f'id: {self.id}, '
            f'title: "{self.title}", '
            f'date: "{self.date}", '
            f'tracks: "{self.tracks}">'
            )

    def load(self, url=None):
        if url:
            logging.debug(f'Url got: {url}')
            self.url = url

        logging.debug(f'{self.url} loading...')

        page = requests.get(url)
        soup = bs(page.text, 'html.parser')

        self.id = int(soup.find(*self.Qualifiers.id).text)
        self.title = soup.find(*self.Qualifiers.title).text.strip()
        self.date = dateutil.parser.parse(soup.find(*self.Qualifiers.date).text.strip()).date()

        nodes = soup.find_all(*self.Qualifiers.song)
        self.raw_tracks = [node.string for node in nodes]

        logging.debug(f'Loaded: "{self.raw_tracks}"')

import logging

from bs4 import BeautifulSoup
import requests

from link import Link


log = logging.getLogger(__name__)


class Loader:
    def __init__(self):
        self.links = []

    def load_links(self, url=None):
        if not url:
            url = 'https://aerostatica.ru/all-volumes/'
        class_ = 'archive-post-title'
        tag = 'a'

        req = requests.get(url)
        data = req.text

        bs = BeautifulSoup(data, 'html.parser')
        for link in bs.find_all(tag, class_=class_):
            href = link.get('href')
            abs_link = Link.toabsolute(url, href)
            self.links.append(abs_link)

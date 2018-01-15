import logging

from config import CONFIG
from link import Link


log = logging.getLogger(__name__)


class Loader:
    def __init__(self, url=None, class_=None, tag=None):
        # Load default attributes from config
        class_name = self.__class__.__name__
        self.url = url or CONFIG.get(class_name, 'url')
        self.class_ = class_ or CONFIG.get(class_name, 'class')
        self.tag = tag or CONFIG.get(class_name, 'tag')

        self.links = []

    def load_links(self):
        req = requests.get(self.url)
        data = req.text

        bs = BeautifulSoup(data, 'html.parser')
        for link in bs.find_all(self.tag, class_=self.class_):
            href = link.get('href')
            abs_link = Link.toabsolute(self.url, href)
            self.links.append(abs_link)

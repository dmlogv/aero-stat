import builtins
import logging

from bs4 import BeautifulSoup
import requests

from config import CONFIG


log = logging.getLogger(__name__)


class Episode:
    def __init__(self, url):
        self.url = url

        self.header = None
        self.date = None
        self.volume = None
        self.tracks = []

        self.load()

    def __repr__(self):
        return (
            '<self.__class__.__name__ ' +
            'header: "self.header" ' +
            'date: "self.date" ' +
            'volume: "self.volume" ' +
            'volume: "self.tracks"' +
            '>'
            ).format(self=self)

    def __str__(self):
        return repr(self)

    def load(self, url=None):
        if url:
            self.url = url

        class_name = self.__class__.__name__
        fields = map(str.strip, CONFIG.get(class_name, 'fields').split(','))

        for field in fields:
            def get(suffix):
                """ Curring of config.get for current field
                """
                return CONFIG.get(class_name, '{}_{}'.format(field, suffix), fallback=None)

            # Get values from config
            source = get('source')
            tag = get('tag')
            class_ = get('class')
            type_ = get('type')
            if source == 'attr':
                attr = get('attr')

            # Parse page
            req = requests.get(self.url)
            data = req.text
            bs = BeautifulSoup(data, 'html.parser')

            # Find values
            for node in bs.find_all(tag, class_=class_):
                if source == 'string':
                    value = node.string
                elif source == 'attr':
                    value = node.get(attr)

                # Trim spaces
                value = value.strip()

                # Convert to specific data type if needed
                if type_:
                    value = getattr(builtins, type_)(value)

                if isinstance(getattr(self, field), list):
                    getattr(self, field).append(value)
                else:
                    setattr(self, field, value)

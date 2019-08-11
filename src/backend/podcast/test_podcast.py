import logging
import unittest

from . import Podcast


logging.basicConfig(level=logging.DEBUG)


class PodcastTest(unittest.TestCase):
    def setUp(self):
        self.podcast = Podcast()

    def test_load(self):
        self.podcast.load(url='https://aerostatica.ru/all-volumes/')
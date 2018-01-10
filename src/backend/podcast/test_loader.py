import unittest
from urllib.parse import urlparse

from loader import Loader


class LoaderTest(unittest.TestCase):
    def setUp(self):
        self.loader = Loader()

    def test_load_links(self):
        self.loader.load_links()
        for link in self.loader.links:
            print(link)
            self.assertTrue(link.startswith('http'))
            self.assertTrue(link.endswith('/'))
            parsed = urlparse(link)
            self.assertTrue(parsed.scheme and parsed.netloc and parsed.path)
import datetime
import logging
import sys
import unittest

from episode import Episode


logging.basicConfig(level=logging.DEBUG)


class EpisodeTest(unittest.TestCase):
    def setUp(self):
        self.episode = Episode('https://aerostatica.ru/2005/05/22/001-zolotoy-vek-muzyki-1/')
        print(self.episode)

    def test_load(self):
        self.assertEqual(1, self.episode.id)
        self.assertEqual('Золотой век музыки - 1', self.episode.title)
        self.assertEqual(datetime.date(2005, 5, 22), self.episode.date)
        self.assertIsInstance(self.episode.raw_tracks, list)

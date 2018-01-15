import unittest

from episode import Episode


class EpisodeTest(unittest.TestCase):
    def setUp(self):
        self.episode = Episode('https://aerostatica.ru/2005/05/22/001-zolotoy-vek-muzyki-1/')
        print(self.episode)

    def test_load(self):
        self.assertEqual('Золотой век музыки - 1', self.episode.header)
        self.assertEqual(1, self.episode.volume)

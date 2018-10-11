import unittest

from track import Track


class TrackTest(unittest.TestCase):
    def setUp(self):
        self.track = Track()

    def test_parsing(self):
        self.track.parse('U2 - The Saints Are Coming')
        self.assertEqual('U2', self.track.artist)
        self.assertEqual('The Saints Are Coming', self.track.name)
import unittest

from link import Link


class LinkTest(unittest.TestCase):
    def test_absolute(self):
        equals = [
            ('http://example.com/root/space', Link.toabsolute('http://example.com/?query', '/root/space')),
            ('http://example.com/root/space', Link.toabsolute('http://example.com', '/root/space')),
            ('http://example.com/root/space', Link.toabsolute('http://example.com/root', 'space')),
            ('http://example.com/root/space', Link.toabsolute('http://example.com', 'root/space'))
            ]
        for expected, actual in equals:
            self.assertEqual(expected, actual)

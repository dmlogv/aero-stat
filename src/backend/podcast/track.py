from artist import Artist


class Track:
    def __init__(self, artists, raw=None):
        self.raw = None

        self.name = None
        self.artist = None

        self.length = None

        if raw:
            self.parse(artists, raw)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name, self.artist))

    def __repr__(self):
        return f'<{self.__class__.__name__} "{self.artist}" — "{self.name}"'

    def parse(self, artists, raw=None):
        if raw:
            self.raw = raw

        artist, self.name = self.raw.split(' - ', maxsplit=1)

        try:
            i = artists.index(artist)
        except ValueError:
            a = Artist(artist)
            artists.append(a)
        else:
            a = artists[i]

        self.artist = a
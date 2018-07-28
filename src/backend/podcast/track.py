class Track:
    def __init__(self, raw=None):
        self.raw = None

        self.name = None
        self.artist = None
        self.length = None

        if raw:
            self.parse(raw)

    def parse(self, raw=None):
        if raw:
            self.raw = raw

        self.artist, self.name = self.raw.split(' - ')

class Artist:
    def __init__(self, name):
        self.name = name
        self.isband = None

        self.tracks = set()

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f'<{self.__class__.__name__} "{self.name}">'

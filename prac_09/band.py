from musician import Musician

class Band(Musician):
    def __init__(self, band):
        super().__init__()
        self.band = band
        self.musician = []

    def __str__(self):
        return f"{self.band} ({self.musician})"

    def __repr__(self):
        return str(vars(self))

    def add(self, musicians):
        self.musician.append(musicians)

    def play(self):
        for i in range(0, len(self.musician)):
            print(f"{self.musician[i]}")
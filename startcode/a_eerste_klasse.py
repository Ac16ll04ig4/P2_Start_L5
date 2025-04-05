class Dier:
    def __init__(self, naam, geluid):
        self.naam = naam
        self.geluid = geluid

    def maak_geluid(self):
        print(f"De {self.naam} zegt '{self.geluid}'.")

hond = Dier("hond", "woef")
hond.maak_geluid()

kat = Dier("kat", "mauw")
kat.maak_geluid()

koe = Dier("koe", "boe")
koe.maak_geluid()
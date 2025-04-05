class Auto:
    def __init__(self,merk, model, jaar):
        self.merk = merk
        self.model = model
        self.jaar = jaar
class Inventaris:
    def __init__(self):
        self.wagens = []
    def voeg_wagen_toe(self, wagen):
        self.wagens.append(wagen)
inventaris = Inventaris()
auto1 = Auto("Volvo", "240", "1984")
auto2 = Auto("Dacia", "Duster", "2021")
inventaris.voeg_wagen_toe(auto1)

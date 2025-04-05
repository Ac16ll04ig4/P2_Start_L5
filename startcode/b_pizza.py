class Pizza:
    def __init__(self,naam,grootte,toppings):
        self.naam = naam
        self.grootte = grootte
        self.toppings = toppings
        self.prijs = self.bereken_prijs()

    def toon_informatie(self):
        print(f"Naam: {self.naam}")
        print(f"Grootte: {self.grootte}")
        for topping in self.toppings:
            print(topping)
        print(f"Prijs: {self.prijs}")

    def bereken_prijs(self):
        basisprijs = 0.0
        if self.grootte == "groot":
            basisprijs = 12.99
        elif self.grootte == "klein":
            basisprijs = 8.99
        basisprijs += len(self.toppings) * 1.5
        return basisprijs


pizza1 = Pizza("Margherita", "klein",["kaas","tomatensaus"])
pizza2 = Pizza("Pepperoni", "groot", ["kaas","tomatensaus","pepperoni"])

pizza1.toon_informatie()
pizza2.toon_informatie()
print(f'prijs: {pizza1.bereken_prijs()}')


import random

class spelare:
    def __init__(self, name, poäng):
        self.name = name
        self.poäng = poäng

    def kasta(self):
        return random.randint(1,6)

    def vin_runda(self):
        self.poäng += 1

spelare1 = spelare("Kalle", 0)
spelare2 = spelare("Erik", 0)

while True:
    res1 = spelare1.kasta()
    res2 = spelare2.kasta()

    print(f"{spelare1.name} slog : {res1}")
    print (f"{spelare2.name} slog : {res2}")

    if res1 > res2:
        spelare1.vin_runda()
        print(f"{spelare1.name} fick poäng!")
    elif res1 < res2:
        spelare2.vin_runda()
        print(f"{spelare2.name} fick poäng!")
    elif res1 == res2:
        print("det blev lika, Inga poäng tilldelade")

    print(f"{spelare1.name} : {spelare1.poäng} poäng")
    print(f"{spelare2.name} : {spelare2.poäng} poäng")

    if spelare1.poäng == 5:
        print(f"{spelare1.name} van!")
        break

    elif spelare2.poäng == 5:
        print(f"{spelare2.name} van!")
        break
class person:
    def __init__(self, förnamn = "", efternamn = "", födelseår = 0):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.födelseår = födelseår

class bil:
    def __init__(self, ägare = None, reg = "", fabrikat = "", årsmodel = "", tjänstevikt = "", motoreffekt = ""):
        self.ägare = ägare
        self.reg = reg
        self.fabrikat = fabrikat
        self.årsmodel = årsmodel
        self.tjänstevikt = tjänstevikt
        self.motoreffekt = motoreffekt

person1 = person("Jasper", "Jamesson", 1997)

bil1 = bil(person1.förnamn, "swag", "BMW", "1956", "7ton", "10kwh")

person2 = person("Casper", "smith", 1851)

bil2 = bil(person2.förnamn, "swag2", "Volvo", "2018", "3.5ton", "8000kwh")


print(f"bil:", bil1.fabrikat, ", ägare:", bil1.ägare, ", registeringnummer:", bil1.reg, ", år:", bil1.årsmodel, ", vikt:", bil1.tjänstevikt, ", kraft:", bil1.motoreffekt)

print(f"bil:", bil2.fabrikat, ", ägare:", bil2.ägare, ", registeringnummer:", bil2.reg, ", år:", bil2.årsmodel, ", vikt:", bil2.tjänstevikt, ", kraft:", bil2.motoreffekt)
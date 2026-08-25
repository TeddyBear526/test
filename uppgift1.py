class person:
    def __init__(self):
        self.förnamn = ""
        self.efternamn = ""
        self.födelseår = ""

class bil:
    def __init__(self):
        self.ägare = None
        self.reg = ''
        self.fabrikat = ''
        self.årsmodel = ''
        self.tjänstevikt = ''
        self.motoreffekt = ''

bil1 = bil()
bil1.ägare = person()
bil1.ägare.förnamn = "bengt"
bil1.reg = 'swag'
bil1.fabrikat = 'BMW'
bil1.årsmodel = '78'
bil1.tjänstevikt = '8ton'
bil1.motoreffekt = '3000kwh'

bil2 = bil()
bil2.ägare = person()
bil2.ägare.förnamn = "mes"
bil2.reg = 'swag2'
bil2.fabrikat = 'Volvo'
bil2.årsmodel = '97'
bil2.tjänstevikt = '3.5ton'
bil2.motoreffekt = '8000kwh'



print(f"bil:", bil1.fabrikat, ", ägare:", bil1.ägare.förnamn, ", registeringnummer:", bil1.reg, ", år:", bil1.årsmodel, ", vikt:", bil1.tjänstevikt, ", kraft:", bil1.motoreffekt)

print(f"bil:", bil2.fabrikat, ", ägare:", bil2.ägare.förnamn, ", registeringnummer:", bil2.reg, ", år:", bil2.årsmodel, ", vikt:", bil2.tjänstevikt, ", kraft:", bil2.motoreffekt)
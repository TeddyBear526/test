class rektangel:
    def __init__(self, x, y, höjd, bredd):
        self.x = x
        self.y = y
        self.höjd = höjd
        self.bredd = bredd

    def sätt_höjd(self, höjd):
        self.höjd = höjd

    def sätt_bredd(self, bredd):
        self.bredd = bredd

    def area(self):
        return self.höjd * self.bredd

    def omkrets(self):
        return 2 * (self.höjd + self.bredd)

r = rektangel(10, 20, 5, 5)

print("Area:", r.area())
print("omkrets", r.omkrets())

r.sätt_höjd(10)
r.sätt_bredd(12)

print("Ny area:", r.area())
print("Ny omkrets:", r.omkrets())
import random

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

rektangel1 = rektangel(10, 20, 5, 5)

for i in range(5):
    rektangel1.sätt_höjd(random.randint(1, 10))
    rektangel1.sätt_bredd(random.randint(1, 10))

    print("Ny area:", rektangel1.area())
    print("Ny omkrets", rektangel1.omkrets())
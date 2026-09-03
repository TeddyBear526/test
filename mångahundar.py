class player:
    def __init__(self):
        self.level = 10
        self.health = 50

    def levelup(self, amount):
        print("Level up!")
        self.level += amount

    def attack(self):
        print("player attacks!")
        self.dealdmg = 10

    def heal(self):
        ("player heals!")

    def walk(self):
        print("player walks")

    def Takedmg(self):
        print("you get attacked!")
        self.health -= 5


class enemy:
    def __init__(self):
        self.level = 10
        self.health = 25

    def attack(self):
        print("player attacks!")
        self.dealdmg = 10

    def heal(self):
        ("player heals!")

    def walk(self):
        print("player walks")

    def Takedmg(self):
        print("you get attacked!")
        self.health -= 5

player1 = player()
enemy1 = enemy()

player1.walk()

player1.attack()
enemy1.Takedmg()
print("enemy health:", enemy1.health)

player1.attack()
enemy1.Takedmg()
print("enemy health:", enemy1.health)

player1.levelup(6)
print("level is :", player1.level)

player1.Takedmg()

print("helth is now", player1.health)
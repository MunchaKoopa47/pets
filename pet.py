import random
class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.xp = 0
        self.level = 0
        self.evolution = 0
        self.is_alive = True
        self.hp = 10

    def eat(self):
        if self.is_alive:
            print(self.name + " goes 'Nom Nom Nom...'")
        else:
            print("Dis boi ded.")

    def sleep(self):
        print("zzzzzzzzzzzzzz...")

    def play(self):
        print("Yipee!")

    def trick(self):
        print("*flips*")

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + \
               ", hp=" + str(self.hp) + \
               ", xp=" + str(self.xp) + \
               ", level=" + str(self.level) + \
               ", evolution=" + str(self.evolution) + "]"        

    def gain_level(self):
        if xp == 10:
            level +=1
            xp = 0

    def evolve(self):
        if level == 15:
            evolution = 1
            level = 0

    def attack(self, other):
        print(self.name + " attacks " + other.name + "!")
        other.hp = other.hp - random.randrange(1, 10)
    
pet1 = Pet("Munchamon")
pet2 = Pet("Coop Dogg")
pet3 = Pet("Bob Ross")
pet4 = Pet("Beanmon")

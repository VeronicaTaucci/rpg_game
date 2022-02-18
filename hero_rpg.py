class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        if enemy.name != "zombie":
            enemy.health -= self.power
        if(self.name == "hero"):
            print(f"You do {self.power} damage to the {enemy.name}.")
        elif (self.name == "goblin" or self.name == "zombie"):
            print(
                f"The {self.name} does {self.power} damage to the {enemy.name} .")

    def print_status(self):
        if self.name == "goblin" or self.name == "zombie":
            print(f"The {self.name} has {self.health} health {self.power} power")
        elif self.name == "hero":
            print(f"You have {self.health} health and {self.power} power")


class Hero(Character):
    def __init__(self, health, power):
        self.name = "hero"
        super(Hero, self).__init__(health, power)


class Goblin(Character):
    def __init__(self, health, power):
        self.name = "goblin"
        super(Goblin, self).__init__(health, power)


class Zombie(Character):
    def __init__(self, health, power):
        self.name = "zombie"
        super(Zombie, self).__init__(health, power)


hero = Hero(10, 5)
goblin = Goblin(6, 2)
zombie = Zombie(10, 1)


def main(enemy):
    while enemy.alive() and hero.alive():
        enemy.print_status
        hero.print_status
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks enemy
            hero.attack(enemy)

            if not enemy.alive():
                print(f"The {enemy.name} is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            # Goblin attacks hero
            enemy.attack(hero)
            if not hero.alive():
                print("You are dead.")


main(zombie)

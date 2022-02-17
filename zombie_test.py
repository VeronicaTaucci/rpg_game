
class Characters:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        if self.health > 0:
            return True
        return False

    def print_status(self):
        print(self.health)


hero = Characters("hero", 10, 5)

##Create a zombie character that cannot die and have it fight the hero instead of the goblin.

zombie = Characters ("zombie", 10, 2)

while zombie.alive() and hero.alive():
    print("You have {} health and {} power.".format(hero.health, hero.power))
    print("The zombie has {} health and {} power.".format(
        zombie.health, zombie.power))
    print()
    print("What do you want to do?")
    print("1. fight zombie")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        # zombie attacks hero
        zombie.attack(hero)
        print("You do {} damage to the hero.".format(zombie.power))
        if hero.health <= 0:
            print("The hero is dead.")
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
    else:
        print("Invalid input {}".format(raw_input))

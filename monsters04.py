class Monster(object):
    def __init__(monster, name, species):
        monster.name = name
        monster.species = species
        monster.hit_points = Monster.initial_hit_points(monster)

    def describe(monster):
        if Monster.is_alive(monster):
            print(
                "{} is a {} with {} hit points".format(
                    monster.name, monster.species, monster.hit_points
                )
            )
        else:
            print("{} is a dead {}".format(monster.name, monster.species))

    def is_alive(monster):
        return monster.hit_points > 0

    def damage(monster, damage_points):
        if Monster.is_alive(monster):
            monster.hit_points -= damage_points
            if not Monster.is_alive(monster):
                print("{} is dead".format(monster.name))
        else:
            print("{} is already dead".format(monster.name))

    def heal(monster):
        if Monster.is_alive(monster):
            monster.hit_points = Monster.initial_hit_points(monster)
        else:
            print("A dead monster cannot be healed")

    def attack(monster, other_monster):
        if Monster.is_alive(monster):
            print("{} attacks {}".format(monster.name, other_monster.name))
            Monster.damage(other_monster, Monster.attack_points(monster))
        else:
            print("A dead monster cannot attack")

    def initial_hit_points(monster):
        if monster.species == "Giant":
            return 10
        elif monster.species == "Dragon":
            return 20
        elif monster.species == "Wyvern":
            return 15
        else:
            assert False

    def attack_points(monster):
        if monster.species == "Giant":
            return 3
        elif monster.species == "Dragon":
            return 4
        elif monster.species == "Wyvern":
            return 5
        else:
            assert False


if __name__ == "__main__":
    gerald = Monster("Gerald", "Giant")
    debbie = Monster("Debbie", "Dragon")
    wallace = Monster("Wallace", "Wyvern")

    Monster.describe(gerald)
    Monster.describe(debbie)
    Monster.attack(debbie, gerald)
    Monster.attack(gerald, debbie)
    Monster.attack(debbie, gerald)
    Monster.attack(gerald, debbie)
    Monster.attack(debbie, gerald)
    Monster.attack(gerald, debbie)
    Monster.describe(gerald)
    Monster.describe(debbie)

def create_monster(name, species):
    monster = Monster()
    monster.name = name
    monster.species = species
    monster.hit_points = initial_hit_points(monster)
    return monster


class Monster(object):
    pass


def describe(monster):
    if is_alive(monster):
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
    if is_alive(monster):
        monster.hit_points -= damage_points
        if not is_alive(monster):
            print("{} is dead".format(monster.name))
    else:
        print("{} is already dead".format(monster.name))


def heal(monster):
    if is_alive(monster):
        monster.hit_points = initial_hit_points(monster)
    else:
        print("A dead monster cannot be healed")


def attack(monster, other_monster):
    if is_alive(monster):
        print("{} attacks {}".format(monster.name, other_monster.name))
        damage(other_monster, attack_points(monster))
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
    gerald = create_monster("Gerald", "Giant")
    debbie = create_monster("Debbie", "Dragon")
    wallace = create_monster("Wallace", "Wyvern")

    describe(gerald)
    describe(debbie)
    attack(debbie, gerald)
    attack(gerald, debbie)
    attack(debbie, gerald)
    attack(gerald, debbie)
    attack(debbie, gerald)
    attack(gerald, debbie)
    describe(gerald)
    describe(debbie)

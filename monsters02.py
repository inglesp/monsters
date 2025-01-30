def create_monster(name, species):
    monster = {
        "name": name,
        "species": species,
    }

    monster["hit_points"] = initial_hit_points(monster)
    return monster


def describe(monster):
    if monster["hit_points"] > 0:
        print(
            "{} is a {} with {} hit points".format(
                monster["name"], monster["species"], monster["hit_points"]
            )
        )
    else:
        print("{} is a dead {}".format(monster["name"], monster["species"]))


def damage(monster, damage_points):
    if monster["hit_points"] > 0:
        monster["hit_points"] -= damage_points
        if monster["hit_points"] <= 0:
            print("{} is dead".format(monster["name"]))
    else:
        print("{} is already dead".format(monster["name"]))


def heal(monster):
    if monster["hit_points"] > 0:
        monster["hit_points"] = initial_hit_points(monster)
    else:
        print("A dead monster cannot be healed")


def initial_hit_points(monster):
    if monster["species"] == "Giant":
        return 10
    elif monster["species"] == "Dragon":
        return 20
    elif monster["species"] == "Wyvern":
        return 15
    else:
        # This is a way of telling Python "this should never happen"
        assert False


def attack(monster, other_monster):
    if monster["hit_points"] > 0:
        print("{} attacks {}".format(monster["name"], other_monster["name"]))
        damage(other_monster, attack_points(monster))
    else:
        print("A dead monster cannot attack")


def attack_points(monster):
    if monster["species"] == "Giant":
        return 3
    elif monster["species"] == "Dragon":
        return 4
    elif monster["species"] == "Wyvern":
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

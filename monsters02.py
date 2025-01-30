# This module introduces a create_monster() function.  It doesn't do much.

# See the full changes with:
#
#   $ diff monsters01.py monsters02.py


def create_monster(name, species):
    return {
        "name": name,
        "species": species,
        "hit_points": initial_hit_points(species),
    }


def describe(monster):
    print(f"{monster['name']} is a ", end="")
    if monster["hit_points"] > 0:
        print(f"{monster['species']} with {monster['hit_points']} hit points")
    else:
        print(f"dead {monster['species']}")


def attack(monster, other_monster):
    if monster["hit_points"] > 0:
        print(f"{monster['name']} attacks {other_monster['name']}")
        damage(other_monster, attack_points(monster))
    else:
        print("A dead monster cannot attack")


def damage(monster, damage_points):
    if monster["hit_points"] > 0:
        monster["hit_points"] -= damage_points
        if monster["hit_points"] > 0:
            print(f"{monster['name']} now has {monster['hit_points']} hit points")
        else:
            print(f"{monster['name']} is dead :(")
    else:
        print(f"{monster['name']} is already dead")


def attack_points(monster):
    if monster["species"] == "dragon":
        return 4
    elif monster["species"] == "giant":
        return 3
    elif monster["species"] == "wyvern":
        return 5
    else:
        # This is a way of telling Python "this should never happen"
        assert False


def initial_hit_points(species):
    if species == "dragon":
        return 20
    elif species == "giant":
        return 10
    elif species == "wyvern":
        return 15
    else:
        assert False


if __name__ == "__main__":
    gerald = create_monster("Gerald", "giant")
    debbie = create_monster("Debbie", "dragon")

    describe(gerald)
    describe(debbie)
    print("-" * 80)
    attack(debbie, gerald)
    print("-" * 80)
    attack(gerald, debbie)
    print("-" * 80)
    attack(debbie, gerald)
    print("-" * 80)
    attack(gerald, debbie)
    print("-" * 80)
    attack(debbie, gerald)
    print("-" * 80)
    describe(gerald)
    describe(debbie)

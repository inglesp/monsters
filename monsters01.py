# This module contains a few functions that operate on dictionaries that
# contain information about individual monsters.

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


if __name__ == "__main__":
    gerald = {
        "name": "Gerald",
        "species": "giant",
        "hit_points": 10,
    }

    debbie = {
        "name": "Debbie",
        "species": "dragon",
        "hit_points": 20,
    }

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

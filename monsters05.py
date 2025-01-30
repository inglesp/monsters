# This module moves our function definitions inside the body of the Monster
# class definition.  (Notice the change in indentation.)
#
# This means that we have to access the functions via eg Monster.describe().
#
# When functions are defined inside the body of a class, we call them
# "methods".  Normal methods always take, as a first parameter, an instance of
# the class.
#
# See the full changes with:
#
#   $ diff monsters04.py monsters05.py


class Monster:
    def __init__(monster, name, species):
        monster.name = name
        monster.species = species
        monster.hit_points = Monster.initial_hit_points(species)

    def describe(monster):
        print(f"{monster.name} is a ", end="")
        if monster.hit_points > 0:
            print(f"{monster.species} with {monster.hit_points} hit points")
        else:
            print(f"dead {monster.species}")

    def attack(monster, other_monster):
        if monster.hit_points > 0:
            print(f"{monster.name} attacks {other_monster.name}")
            Monster.damage(other_monster, Monster.attack_points(monster))
        else:
            print("A dead monster cannot attack")

    def damage(monster, damage_points):
        if monster.hit_points > 0:
            monster.hit_points -= damage_points
            if monster.hit_points > 0:
                print(f"{monster.name} now has {monster.hit_points} hit points")
            else:
                print(f"{monster.name} is dead :(")
        else:
            print(f"{monster.name} is already dead")

    def attack_points(monster):
        if monster.species == "dragon":
            return 4
        elif monster.species == "giant":
            return 3
        elif monster.species == "wyvern":
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
    gerald = Monster("Gerald", "giant")
    debbie = Monster("Debbie", "dragon")

    Monster.describe(gerald)
    Monster.describe(debbie)
    print("-" * 80)
    Monster.attack(debbie, gerald)
    print("-" * 80)
    Monster.attack(gerald, debbie)
    print("-" * 80)
    Monster.attack(debbie, gerald)
    print("-" * 80)
    Monster.attack(gerald, debbie)
    print("-" * 80)
    Monster.attack(debbie, gerald)
    print("-" * 80)
    Monster.describe(gerald)
    Monster.describe(debbie)

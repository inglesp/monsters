# In this module we change how we call methods.
#
# When methods take, as a first parameter, an instance of the class on which
# they are defined, it is more usual to call the method by looking up the
# method as if it were an attribute on the instance, and then calling it as it
# were a function.
#
# That is, if object i is an instance of class C, then these are equivalent:
#
#   C.method(i, argument)
#   i.method(argument)

# See the full changes with:
#
#   $ diff monsters05.py monsters06.py


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
            other_monster.damage(monster.attack_points())
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

    gerald.describe()
    debbie.describe()
    print("-" * 80)
    debbie.attack(gerald)
    print("-" * 80)
    gerald.attack(debbie)
    print("-" * 80)
    debbie.attack(gerald)
    print("-" * 80)
    gerald.attack(debbie)
    print("-" * 80)
    debbie.attack(gerald)
    print("-" * 80)
    gerald.describe()
    debbie.describe()

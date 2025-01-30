# This module introduces an (empty) Monster class.
#
# Instead of working with dictionaries we now work with instances of this
# class (which we call "objects").  This means we use Python's dot notation to
# look up attributes of the objects, rather than using the square bracket
# notation to look up keys in a dictionary.
#
# But we haven't really lost the dictionaries!  Python objects are thin
# wrappers around dictionaries, and we can recover the dictionaries by looking
# at an object's .__dict__ attribute.
#
#   >>> import monsters03
#   >>> g = monsters03.create_monster("Gerald", "giant")
#   >>> g.__dict__
#   {'name': 'Gerald', 'species': 'giant', 'hit_points': 10}
#
# Creating an instance of the class ("instantiating the class") looks a bit
# like calling a function:
#
#   >>> monsters03.Monster()
#   <monsters03.Monster object at 0x7929ca368310>
#
# The peculiar thing in angular brackets is Python's default way of showing us
# an object.  We see the object's class and the module it was defined in, as
# well as its location in memory.

# See the full changes with:
#
#   $ diff monsters02.py monsters03.py


class Monster:
    pass


def create_monster(name, species):
    monster = Monster()
    monster.name = name
    monster.species = species
    monster.hit_points = initial_hit_points(species)
    return monster


def describe(monster):
    print(f"{monster.name} is a ", end="")
    if monster.hit_points > 0:
        print(f"{monster.species} with {monster.hit_points} hit points")
    else:
        print(f"dead {monster.species}")


def attack(monster, other_monster):
    if monster.hit_points > 0:
        print(f"{monster.name} attacks {other_monster.name}")
        damage(other_monster, attack_points(monster))
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

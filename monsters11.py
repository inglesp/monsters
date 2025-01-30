# In this module we introduce class variables.
#
# These are variables that are defined in the body of a class definition.  They
# can be accessed either as attributes of a class, or as attributes of an
# instance of a class:
#
#   >>> import monsters11
#   >>> monsters11.Dragon.attack_points
#   4
#   >>> d = monsters11.Dragon("Debbie")
#   >>> d.attack_points
#   4
#
# attack_points is not in d's dictionary of attributes:
#
#   >>> d.__dict__
#   {'name': 'Debbie', 'species': 'dragon', 'hit_points': 20}
#
# But classes also have dictionaries of attributes, and it is there:
#
#   >>> monsters11.Dragon.__dict__
#   mappingproxy({'__module__': 'monsters11', 'attack_points': 4, '__init__': <function Dragon.__init__ at 0x7c73dc2bda20>, 'describe_attack': <function Dragon.describe_attack at 0x7c73dc2bdab0>, '__doc__': None})
#
# (What else can you see there?)

# See the full changes with:
#
#   $ diff monsters10.py monsters11.py


class Monster:
    def describe(monster):
        print(f"{monster.name} is a ", end="")
        if monster.hit_points > 0:
            print(f"{monster.species} with {monster.hit_points} hit points")
        else:
            print(f"dead {monster.species}")

    def attack(monster, other_monster):
        if monster.hit_points > 0:
            monster.describe_attack(other_monster)
            other_monster.damage(monster.attack_points)
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


class Dragon(Monster):
    attack_points = 4

    def __init__(monster, name):
        monster.name = name
        monster.species = "dragon"
        monster.hit_points = 20

    def describe_attack(monster, other_monster):
        print(f"{monster.name} breathes fire on {other_monster.name}")


class Giant(Monster):
    attack_points = 3

    def __init__(monster, name):
        monster.name = name
        monster.species = "giant"
        monster.hit_points = 10

    def describe_attack(monster, other_monster):
        print(f"{monster.name} swings a club at {other_monster.name}")


class Wyvern(Monster):
    attack_points = 5

    def __init__(monster, name):
        monster.name = name
        monster.species = "wyvern"
        monster.hit_points = 15

    def describe_attack(monster, other_monster):
        print(f"{monster.name} swipes at {other_monster.name} with its tail")


if __name__ == "__main__":
    gerald = Giant("Gerald")
    debbie = Dragon("Debbie")

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

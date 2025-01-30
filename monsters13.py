# In this module we move the __init__ method back to the base class, since it
# is the same for each subclass.

# See the full changes with:
#
#   $ diff monsters12.py monsters13.py


class Monster:
    def __init__(monster, name):
        monster.name = name
        monster.hit_points = monster.initial_hit_points

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
    species = "dragon"
    initial_hit_points = 20
    attack_points = 4

    def describe_attack(monster, other_monster):
        print(f"{monster.name} breathes fire on {other_monster.name}")


class Giant(Monster):
    species = "giant"
    initial_hit_points = 10
    attack_points = 3

    def describe_attack(monster, other_monster):
        print(f"{monster.name} swings a club at {other_monster.name}")


class Wyvern(Monster):
    species = "wyvern"
    initial_hit_points = 15
    attack_points = 5

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

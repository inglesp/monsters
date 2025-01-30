# In this monster we rename the "monster" parameter to "self".
#
# It is conventional in Python to name the first argument to a method "self".
# But the name is nothing special -- up to now, we've called it "monster".
#
# See the full changes with:
#
#   $ diff monsters13.py monsters14.py


class Monster:
    def __init__(self, name):
        self.name = name
        self.hit_points = self.initial_hit_points

    def describe(self):
        print(f"{self.name} is a ", end="")
        if self.hit_points > 0:
            print(f"{self.species} with {self.hit_points} hit points")
        else:
            print(f"dead {self.species}")

    def attack(self, other_monster):
        if self.hit_points > 0:
            self.describe_attack(other_monster)
            other_monster.damage(self.attack_points)
        else:
            print("A dead monster cannot attack")

    def damage(self, damage_points):
        if self.hit_points > 0:
            self.hit_points -= damage_points
            if self.hit_points > 0:
                print(f"{self.name} now has {self.hit_points} hit points")
            else:
                print(f"{self.name} is dead :(")
        else:
            print(f"{self.name} is already dead")


class Dragon(Monster):
    species = "dragon"
    initial_hit_points = 20
    attack_points = 4

    def describe_attack(self, other_monster):
        print(f"{self.name} breathes fire on {other_monster.name}")


class Giant(Monster):
    species = "giant"
    initial_hit_points = 10
    attack_points = 3

    def describe_attack(self, other_monster):
        print(f"{self.name} swings a club at {other_monster.name}")


class Wyvern(Monster):
    species = "wyvern"
    initial_hit_points = 15
    attack_points = 5

    def describe_attack(self, other_monster):
        print(f"{self.name} swipes at {other_monster.name} with its tail")


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


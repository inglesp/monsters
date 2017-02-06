class Monster(object):
    def __init__(self, name):
        self.name = name
        self.species = type(self).__name__
        self.hit_points = self.initial_hit_points

    def describe(self):
        if self.is_alive():
            print('{} is a {} with {} hit points'.format(self.name, self.species, self.hit_points))
        else:
            print('{} is a dead {}'.format(self.name, self.species))

    def is_alive(self):
        return self.hit_points > 0

    def damage(self, damage_points):
        if self.is_alive():
            self.hit_points -= damage_points
            if not self.is_alive():
                print('{} is dead'.format(self.name))
        else:
            print('{} is already dead'.format(self.name))

    def heal(self):
        if self.is_alive():
            self.hit_points = self.initial_hit_points
        else:
            print('A dead self cannot be healed')

    def attack(self, other):
        if self.is_alive():
            self.describe_attack(other)
            other.damage(self.attack_points)
        else:
            print('A dead self cannot attack')


class Giant(Monster):
    initial_hit_points = 10
    attack_points = 3

    def describe_attack(self, other):
        print('{} swings a club at {}'.format(self.name, other.name))


class Dragon(Monster):
    initial_hit_points = 20
    attack_points = 4

    def describe_attack(self, other):
        print('{} breathes fire on {}'.format(self.name, other.name))


class Wyvern(Monster):
    initial_hit_points = 15
    attack_points = 5

    def describe_attack(self, other):
        print('{} swipes at {} with its tail'.format(monster.name, other_monster.name))


class Ogre(Giant):
    initial_hit_points = 10
    attack_points = 5

    def describe_attack(self, other):
        print('{} charges at {} with a spear'.format(self.name, other.name))


if __name__ == '__main__':
    gerald = Giant('Gerald')
    debbie = Dragon('Debbie')
    wallace = Wyvern('Wallace')
    olivia = Ogre('Olivia')

    gerald.describe()
    olivia.describe()
    olivia.attack(gerald)
    gerald.attack(olivia)
    olivia.attack(gerald)
    gerald.attack(olivia)
    olivia.attack(gerald)
    olivia.describe()

class Monster(object):
    def describe(monster):
        if monster.is_alive():
            print('{} is a {} with {} hit points'.format(monster.name, monster.species, monster.hit_points))
        else:
            print('{} is a dead {}'.format(monster.name, monster.species))

    def is_alive(monster):
        return monster.hit_points > 0

    def damage(monster, damage_points):
        if monster.is_alive():
            monster.hit_points -= damage_points
            if not monster.is_alive():
                print('{} is dead'.format(monster.name))
        else:
            print('{} is already dead'.format(monster.name))

    def heal(monster):
        if monster.is_alive():
            monster.hit_points = monster.initial_hit_points
        else:
            print('A dead monster cannot be healed')

    def attack(monster, other_monster):
        if monster.is_alive():
            monster.describe_attack(other_monster)
            other_monster.damage(monster.attack_points)
        else:
            print('A dead monster cannot attack')


class Giant(Monster):
    initial_hit_points = 10
    attack_points = 3

    def __init__(monster, name):
        monster.name = name
        monster.species = 'Giant'
        monster.hit_points = monster.initial_hit_points

    def describe_attack(monster, other_monster):
        print('{} swings a club at {}'.format(monster.name, other_monster.name))


class Dragon(Monster):
    initial_hit_points = 20
    attack_points = 4

    def __init__(monster, name):
        monster.name = name
        monster.species = 'Dragon'
        monster.hit_points = monster.initial_hit_points

    def describe_attack(monster, other_monster):
        print('{} breathes fire on {}'.format(monster.name, other_monster.name))


class Wyvern(Monster):
    initial_hit_points = 15
    attack_points = 5

    def __init__(monster, name):
        monster.name = name
        monster.species = 'Wyvern'
        monster.hit_points = monster.initial_hit_points

    def describe_attack(monster, other_monster):
        print('{} swipes at {} with its tail'.format(monster.name, other_monster.name))


if __name__ == '__main__':
    gerald = Giant('Gerald')
    debbie = Dragon('Debbie')
    wallace = Wyvern('Wallace')

    gerald.describe()
    debbie.describe()
    debbie.attack(gerald)
    gerald.attack(debbie)
    debbie.attack(gerald)
    gerald.attack(debbie)
    debbie.attack(gerald)
    gerald.attack(debbie)
    gerald.describe()
    debbie.describe()

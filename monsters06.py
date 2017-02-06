class Monster(object):
    def __init__(monster, name, species):
        monster.name = name
        monster.species = species
        monster.hit_points = monster.initial_hit_points()

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
            monster.hit_points = monster.initial_hit_points()
        else:
            print('A dead monster cannot be healed')

    def attack(monster, other_monster):
        if monster.is_alive():
            if monster.species == 'Giant':
                print('{} swings a club at {}'.format(monster.name, other_monster.name))
            elif monster.species == 'Dragon':
                print('{} breathes fire on {}'.format(monster.name, other_monster.name))
            elif monster.species == 'Wyvern':
                print('{} swipes at {} with its tail'.format(monster.name, other_monster.name))
            else:
                assert False

            other_monster.damage(monster.attack_points())
        else:
            print('A dead monster cannot attack')

    def initial_hit_points(monster):
        if monster.species == 'Giant':
            return 10
        elif monster.species == 'Dragon':
            return 20
        elif monster.species == 'Wyvern':
            return 15
        else:
            assert False

    def attack_points(monster):
        if monster.species == 'Giant':
            return 3
        elif monster.species == 'Dragon':
            return 4
        elif monster.species == 'Wyvern':
            return 5
        else:
            assert False


if __name__ == '__main__':
    gerald = Monster('Gerald', 'Giant')
    debbie = Monster('Debbie', 'Dragon')
    wallace = Monster('Wallace', 'Wyvern')

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

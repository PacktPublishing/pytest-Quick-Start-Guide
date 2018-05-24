import textwrap
from math import sqrt


def magnitude(x, y):
    return sqrt(x * x + y * y)


def starting_coords():
    return 2.2, 3.6


def test_magnitude():
    x, y = starting_coords()
    assert magnitude(x, y) == 8.5


def get_default_player_class():
    return 'warrior'


def test_default_player_class():
    x = get_default_player_class()
    assert x == 'sorcerer'


def get_short_class_description(class_name):
    assert class_name == 'warrior'
    return 'A battle-hardened veteran, favors heavy armor and weapons.'


def test_warrior_short_description():
    desc = get_short_class_description('warrior')
    assert desc == 'A battle-hardened veteran, can equip heavy armor and weapons.'


def get_long_class_description(class_name):
    assert class_name == 'warrior'
    return textwrap.dedent('''\
    A seasoned veteran of many battles. High Strength and Dexterity
    allow to yield heavy armor and weapons, as well as carry
    more equipment while keeping a light roll. Weak in magic.            
    ''')


def test_warrior_long_description():
    desc = get_long_class_description('warrior')
    assert desc == textwrap.dedent('''\
        A seasoned veteran of many battles. Strength and Dexterity
        allow to yield heavy armor and weapons, as well as carry
        more equipment. Weak in magic.            
        ''')

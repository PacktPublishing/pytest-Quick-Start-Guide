import textwrap
from math import sqrt

from pytest import approx


def magnitude(x, y):
    return sqrt(x * x + y * y)


def test_simple_math():
    assert abs(0.1 + 0.2) - 0.3 < 0.0001


def test_simple_math2():
    assert (-0.1 - 0.2) + 0.3 < 0.0001


def test_approx_simple():
    assert 0.1 + 0.2 == approx(0.3)


def test_approx_list():
    assert [0.1 + 1.2, 0.2 + 0.8] == approx([1.3, 1.0])


def test_approx_dict():
    values = {"v1": 0.1 + 1.2, "v2": 0.2 + 0.8}
    assert values == approx(dict(v1=1.3, v2=1.0))


def test_approx_simple_fail():
    assert 0.1 + 0.2 == approx(0.35)


def test_approx_list_fail():
    assert [0.1 + 1.2, 0.2 + 0.8] == approx([1.3, 1.1])


def test_approx_numpy():
    import numpy as np

    values = np.array([0.1, 0.2]) + np.array([1.2, 0.8])
    assert values == approx(np.array([1.3, 1.0]))


def test_magnitude_plain():
    assert abs(magnitude(8.0, 20.0) - 21.540659) < 0.00001


def test_magnitude():
    assert magnitude(8.0, 20.0) == approx(21.540659)


def get_default_health(class_name):
    assert class_name == "warrior"
    return 80


def test_default_health():
    health = get_default_health("warrior")
    assert health == 95


def get_default_player_class():
    return "warrior"


def test_default_player_class():
    x = get_default_player_class()
    assert x == "sorcerer"


def get_short_class_description(class_name):
    assert class_name == "warrior"
    return "A battle-hardened veteran, favors heavy armor and weapons."


def test_warrior_short_description():
    desc = get_short_class_description("warrior")
    assert (
        desc
        == "A battle-hardened veteran, can equip heavy armor and weapons."
    )


def get_long_class_description(class_name):
    assert class_name == "warrior"
    return textwrap.dedent(
        """\
    A seasoned veteran of many battles. High Strength and Dexterity
    allow to yield heavy armor and weapons, as well as carry
    more equipment while keeping a light roll. Weak in magic.            
    """
    )


def test_warrior_long_description():
    desc = get_long_class_description("warrior")
    assert (
        desc
        == textwrap.dedent(
            """\
        A seasoned veteran of many battles. Strength and Dexterity
        allow to yield heavy armor and weapons, as well as carry
        more equipment. Weak in magic.            
        """
        )
    )


def get_starting_equipment(class_name):
    assert class_name == "warrior"
    return ["long sword", "warrior set", "shield"]


def test_get_starting_equiment():
    expected = ["long sword", "shield"]
    assert get_starting_equipment("warrior") == expected


def test_long_list():
    x = [str(i) for i in range(100)]
    y = [str(i) for i in range(0, 100, 2)]
    assert x == y


def get_classes_starting_health():
    return {"warrior": 85, "sorcerer": 55, "knight": 95}


def test_starting_health():
    expected = {"warrior": 85, "sorcerer": 50}
    assert get_classes_starting_health() == expected


def get_player_classes():
    return {"warrior", "knight", "sorcerer"}


def test_player_classes():
    assert get_player_classes() == {"warrior", "sorcerer"}

import pytest


class InvalidCharacterNameError(Exception):
    pass


class InvalidClassNameError(Exception):
    pass


class Character:
    pass


VALID_CLASSES = ["sorcerer", "warrior"]


def create_character(name: str, class_name: str) -> Character:
    """
    Creates a new character and inserts it into the database.

    :param name: the character name.

    :param class_name: the character class name.

    :raise InvalidCharacterNameError:
        if the character name is empty.

    :raise InvalidClassNameError:
        if the class name is invalid.

    :return: the newly created Character.
    """
    if not name:
        raise InvalidCharacterNameError("character name empty")

    if class_name not in VALID_CLASSES:
        msg = f'invalid class name: "{class_name}"'
        raise InvalidCharacterNameError(msg)
    ...


def test_empty_name():
    with pytest.raises(InvalidCharacterNameError):
        create_character(name="", class_name="warrior")


def test_invalid_class_name():
    with pytest.raises(InvalidClassNameError):
        create_character(name="Solaire", class_name="mage")


def test_empty_name():
    with pytest.raises(
        InvalidCharacterNameError, match="character name empty"
    ):
        create_character(name="", class_name="warrior")


def test_invalid_class_name():
    with pytest.raises(
        InvalidClassNameError, match='invalid class name: "mage"'
    ):
        create_character(name="Solaire", class_name="mage")

import pytest

from sivtools.utilities import deconstruct


def test_deconstruct_one_item():
    # Arrange
    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    # Act
    key1, result = deconstruct(my_dict, 'key1')

    # Assert
    assert key1 == 'value1'
    assert result == {'key2': 'value2', 'key3': 'value3'}


def test_deconstruct_one_item_key_does_not_exist():
    # Arrange
    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    # Act - Assert
    with pytest.raises(KeyError):
        deconstruct(my_dict, 'bad_key')


def test_deconstruct_multiple_items():
    # Arrange
    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    # Act
    key1, key2, result = deconstruct(my_dict, ['key1', 'key2'])

    # Assert
    assert key1 == 'value1'
    assert key2 == 'value2'
    assert result == {'key3': 'value3'}


def test_deconstruct_multiple_items_key_does_not_exist():
    # Arrange
    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    # Act - Assert
    with pytest.raises(KeyError):
        deconstruct(my_dict, ['key1', 'bad_key'])

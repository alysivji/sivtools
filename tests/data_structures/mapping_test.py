import pytest

from sivtools.data_structures import DotDict


def test_dotdict_get_item_by_key():
    sample_dict = {}
    sample_dict["item"] = "value"

    my_dict = DotDict(sample_dict)

    assert my_dict.item == "value"


def test_dotdict_nested():
    inside_dict = {}
    inside_dict["inner_item"] = "inner value"

    sample_dict = {}
    sample_dict["item"] = inside_dict

    my_dict = DotDict(sample_dict)

    assert my_dict.item.inner_item == "inner value"


def test_create_dotdict_with_non_mapping():
    """
    Creating a DotDict using a non-mapping type results in an error
    """

    with pytest.raises(TypeError, message="Requires mapping type"):
        DotDict([1, 2, 3])


def test_accessing_keyword_element():
    """
    Unallowed attribute is identfied and stored appropriately
    """

    sample_dict = {}
    sample_dict["1str"] = "value"

    my_dict = DotDict(sample_dict)

    assert "1str" in my_dict.unallowed_attributes

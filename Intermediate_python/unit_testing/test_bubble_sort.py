from sort_algorithms.bubble_sort import bubble_sort
import pytest


def test_bubble_sort_with_a_small_list():
    #Arrange
    list_to_sort_input = [6, 5, 8, 3]
    #Act
    result = bubble_sort(list_to_sort_input)
    #Assert
    assert result == [3, 5, 6, 8]


def test_bubble_sort_with_a_big_list():

    list_to_sort_input = list(range(150, 0, -1))
    sort_result = bubble_sort(list_to_sort_input)
    expected_result = sorted(list_to_sort_input)

    assert sort_result == expected_result


def test_bubble_sort_with_empty_list():
    empty_list = bubble_sort([])
    assert empty_list == []



@pytest.mark.parametrize("Invalid_input", [
    10,
    10.5,
    "Hello",
    (1, 3, 2),
    {"a": 1},
    None
])
def test_bubble_sort_with_no_list_as_a_parameter(Invalid_input):

    with pytest.raises(TypeError):
        bubble_sort(Invalid_input)
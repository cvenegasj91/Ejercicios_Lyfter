from Python_basics.funtions import Excercise_03, Excercise_04, Excercise_05, Excercise_06, Excercise_07
import pytest

def test_sum_numbers_with_small_numbers():
    
    sum = [10, 35, 25, 5]
    sum = Excercise_03.sum_numbers(sum)
    
    assert sum == 75


def test_sum_numbers_with_big_numbers():

    sum = [45250, 5500, 35450, 75490]
    sum = Excercise_03.sum_numbers(sum)
        
    assert sum == 161690


def test_sum_numbers_with_negative_numbers():

    sum = [-45250, -5500, -35450, -75490]
    sum = Excercise_03.sum_numbers(sum)
        
    assert sum == -161690


def test_revert_string():

    my_string = "Carlos"
    my_string = Excercise_04.revert_list(my_string)

    assert my_string == "solraC"


def test_revert_string_with_empty_string():

    my_string = ""
    my_string = Excercise_04.revert_list(my_string)

    assert my_string == ""


@pytest.mark.parametrize("Invalid_input", [
    10,
    10.5,
    {"a": 1},
    (1, 2, 3),
    [1, 2, 3],
    None
])
def test_revert_string_with_no_string_as_a_parameter(Invalid_input):

    with pytest.raises(TypeError):
        Excercise_04.revert_list(Invalid_input)


def test_lowers_capitals_counter():

    text = "Hola Mundo"
    capitals, lowers = Excercise_05.lowers_capitatls_counter(text)

    assert capitals == 2 and lowers == 7


def test_lowers_and_capitals_counter_with_latin_characters():
    text = "áÁ Éé ñÑ"
    capitals, lowers = Excercise_05.lowers_capitatls_counter(text)
    
    assert capitals == 3 and lowers == 3


def test_lowers_and_capitals_counter_with_no_string_as_a_parameter():
    text = "áÁ Éé ñÑ"
    capitals, lowers = Excercise_05.lowers_capitatls_counter(text)
    
    assert capitals == 3 and lowers == 3


@pytest.mark.parametrize("Invalid_input2", [
    10,
    10.5,
    {"a": 1},
    (1, 2, 3),
    [1, 2, 3],
    None
])
def test_lowers_and_capitals_counter_with_no_string_as_a_parameter(Invalid_input2):

    with pytest.raises(TypeError):
        Excercise_05.lowers_capitatls_counter(Invalid_input2)


def test_sort_words_AZ():

    text = "Carrot-Banana-Apple"
    result = Excercise_06.sort_words_AZ(text)

    assert result == "Apple-Banana-Carrot"


def test_sort_words_AZ_with_alreaddy_sorted_words():

    text = "Apple-Banana-Carrot"
    result = Excercise_06.sort_words_AZ(text)

    assert result == "Apple-Banana-Carrot"


def test_sort_words_AZ_with_repeted_words():

    text = "Apple-Banana-Carrot-Banana-Apple"
    result = Excercise_06.sort_words_AZ(text)

    assert result == "Apple-Apple-Banana-Banana-Carrot"


def test_calculate_prime_numb():

    numbers = [3, 1, 2, 6, 9, 79]
    result = Excercise_07.calculate_prime_numb(numbers)

    assert result == [3, 2, 79]


def test_calculate_prime_numb_with_only_primes():

    numbers = [3, 2, 79]
    result = Excercise_07.calculate_prime_numb(numbers)

    assert result == [3, 2, 79]


def test_calculate_prime_numb_with_no_primes():

    numbers = [1, 6, 9]
    result = Excercise_07.calculate_prime_numb(numbers)

    assert result == []
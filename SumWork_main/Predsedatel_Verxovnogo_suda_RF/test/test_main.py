from My_source.main import Calculation, Text_Greeting
import pytest

@pytest.mark.calc
def test_sum():
    assert Calculation().sum(22, 11) == 33

@pytest.mark.skip
def test_invisible():
    assert 33 == 5

@pytest.mark.calc
def test_sub():
    assert Calculation().sub(18, 3) == 15

@pytest.mark.calc
def test_multiply():
    assert Calculation().multiply(5, 5) == 25

@pytest.mark.calc
def test_string_check():
    assert Calculation().string_check('my_string_check') == 'MY_STRING_CHECK'

@pytest.mark.calc
def test_bool_check():
    assert Calculation().bool_check(True)

@pytest.mark.calc
def div():
    assert Calculation().div(40,2) == 20

@pytest.mark.calc
def test_fplayn():
    assert Calculation().find_palyndrome(True)

@pytest.mark.calc
@pytest.mark.skip('не трогать не работает')
def test_skip():
    assert 33 == 5

@pytest.mark.calc
def test_bool_check():
    assert Calculation().boole(True)

    "TEXT GREETING"

@pytest.mark.greet
def test_string():
    assert Text_Greeting().register_check('jo_check_str') == 'jo_check_str'.upper()

@pytest.mark.calc
@pytest.mark.parametrize('test_input, expected', [('Мухаджан', 'my name Мухаджан'), ('Ахмед', 'my name Ахмед')])
def test_greeting(test_input, expected):
    assert Text_Greeting().greeting(test_input) == expected

@pytest.mark.greet
def test_check():
    assert Text_Greeting().empty_string(True)

@pytest.mark.greet
def test_long():
    assert Text_Greeting().long_check(True)

@pytest.mark.greet
def test_type():
    assert Text_Greeting().string_type(True)

@pytest.mark.skip
def test_empty():
    assert 'Aboba' == 'Anton'
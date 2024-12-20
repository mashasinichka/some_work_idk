from My_source.my_pow import Pow
from My_source.my_pow import find_fibonacci
import pytest
import math

@pytest.mark.pow2
def test_pow2():
    assert Pow().pow2(5) == 25

@pytest.mark.pow2
def test_pow2_match():
    assert Pow().pow2_math(3) == 9

@pytest.mark.pow3
def test_pow3_math():
    assert Pow().pow3_math(5) == 125

@pytest.mark.fibonacci
def test_fibonacci():
    assert find_fibonacci(6) == 8

@pytest.mark.pow3
def test_notpow():
    assert 33 == 5





import pytest

from ejercicios.ejercicio2 import factorial


def test_factorial_de_cero():
    assert factorial(0) == 1, "Por definición, 0! = 1"


def test_factorial_de_uno():
    assert factorial(1) == 1


def test_factorial_de_cinco():
    assert factorial(5) == 120, "5! = 5*4*3*2*1 = 120"


def test_factorial_grande():
    assert factorial(10) == 3628800


def test_negativo_lanza_error():
    with pytest.raises(ValueError):
        factorial(-1)

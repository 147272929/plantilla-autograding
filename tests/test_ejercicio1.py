from ejercicios.ejercicio1 import contar_pares


def test_lista_mixta():
    assert contar_pares([1, 2, 3, 4]) == 2, "En [1, 2, 3, 4] hay 2 pares"


def test_lista_vacia():
    assert contar_pares([]) == 0, "Una lista vacía tiene 0 pares"


def test_negativos_y_cero():
    assert contar_pares([-2, 0, 7]) == 2, "-2 y 0 también son pares"


def test_sin_pares():
    assert contar_pares([1, 3, 5]) == 0, "En [1, 3, 5] no hay pares: debe devolver 0"

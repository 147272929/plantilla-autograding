from ejercicios.ejercicio3 import es_palindromo


def test_frase_palindromo():
    assert es_palindromo("Anita lava la tina") is True, "Debe ignorar espacios y mayúsculas"


def test_no_palindromo():
    assert es_palindromo("Programación") is False, '"Programación" no es palíndromo: debe devolver False'


def test_texto_vacio():
    assert es_palindromo("") is True, "El texto vacío se considera palíndromo"


def test_con_tildes():
    assert es_palindromo("Allí ves Sevilla") is True, '"Allí ves Sevilla" es palíndromo: debes ignorar las tildes (í = i)'

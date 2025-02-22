import pytest
from calculadora import sumar, dividir

@pytest.mark.parametrize("a, b, esperado", [
    (1, 2, 3),
    (2, -2, 0),
    (0, 1, 1)
])
def test_suma(a, b, esperado):
    assert sumar(a, b) == esperado

def test_division():
    assert dividir(4, 2) == 2
    with pytest.raises(ValueError):
        dividir(8, 0)

import pytest
from calculadora import sumar, restar, dividir

#  función sumar
@pytest.mark.parametrize("a, b, esperado", [
    (1, 2, 3),      # Suma básica
    (2, -2, 0),     # Suma con número negativo
    (0, 0, 0),      # Suma de ceros
])
def test_sumar(a, b, esperado):
    assert sumar(a, b) == esperado

# función restar
@pytest.mark.parametrize("a, b, esperado", [
    (5, 3, 2),      # Resta básica
    (0, 0, 0),      # Resta de ceros
    (-5, -3, -2),   # Resta de números negativos
])
def test_restar(a, b, esperado):
    assert restar(a, b) == esperado

# función dividir
def test_dividir():
    assert dividir(10, 2) == 5  
    assert dividir(0, 5) == 0   
    with pytest.raises(ValueError):
        dividir(8, 0)  # División por cero
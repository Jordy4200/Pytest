import pytest
from factorial import factorial_iterative, factorial_recursive

# Pruebas para factorial iterativo
@pytest.mark.parametrize("n, esperado", [
    (0, 1),  
    (1, 1),  
    (5, 120), # Factorial de 5
    (10, 3628800), # Factorial de 10
])
def test_factorial_iterative(n, esperado):
    assert factorial_iterative(n) == esperado

# Pruebas para factorial recursivo
@pytest.mark.parametrize("n, esperado", [
    (0, 1),  
    (1, 1),  
    (5, 120), # Factorial de 5
    (10, 3628800), # Factorial de 10
])
def test_factorial_recursive(n, esperado):
    assert factorial_recursive(n) == esperado
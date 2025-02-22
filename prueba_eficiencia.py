import time
import pytest
from analisis_eficiencia import fibonacci, permutaciones

# Prueba de eficiencia para Fibonacci
def test_fibonacci():
    inicio = time.time()
    assert fibonacci(35) == 9227465  
    fin = time.time()
    print(f"Tiempo de ejecución de Fibonacci: {fin - inicio} segundos")

# Prueba de eficiencia para permutaciones
def test_permutaciones():
    inicio = time.time()
    assert len(permutaciones([1, 2, 3])) == 6  
    fin = time.time()
    print(f"Tiempo de ejecución de permutaciones: {fin - inicio} segundos")
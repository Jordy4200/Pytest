import time

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):  # Orden de complejidad:
        result *= i
    return result

def factorial_recursive(n):
    if n == 1 or n == 0: return 1
    return n * factorial_recursive(n - 1)

inicio = time.time()
print(factorial_iterative(20))
fin = time.time()
print("Tiempo de ejecución iterativo:", fin - inicio)

inicio = time.time()
print(factorial_recursive(20))
fin = time.time()
print("Tiempo de ejecución recursivo:", fin - inicio)

from prueba_ordenamiento import merge_sort

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Nueva prueba cambiando valores en los arreglos
print("Linear search:")
arr = [78, 55, 23, 19, 45, 90, 2]
print(linear_search(arr, 45))  # Buscamos un número diferente

print("\nBinary search:")
arr = [78, 55, 23, 19, 45, 90, 2]
merge_sort(arr)  # Usamos la versión de merge_sort de prueba_ordenamiento
print(binary_search_iterative(arr, 55))  # Buscamos otro número

print("\nBinary search (recursivo):")
arr = [78, 55, 23, 19, 45, 90, 2]
merge_sort(arr)
print(binary_search_recursive(arr, 19, 0, len(arr) - 1))  # Buscamos otro valor

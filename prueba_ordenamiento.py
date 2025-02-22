def bubble_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)
    return arr

def selection_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        print(arr)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    print(arr)
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        print(left_half, right_half)
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Nuevas pruebas cambiando valores
print("-------- Bubble Sort --------")
arr = [42, 89, 17, 56, 33, 10, 91]
print(bubble_sort(arr))

print("-------- Selection Sort --------")
arr = [42, 89, 17, 56, 33, 10, 91]
print(selection_sort(arr))

print("-------- Insertion Sort --------")
arr = [42, 89, 17, 56, 33, 10, 91]
print(insertion_sort(arr))

print("-------- Merge Sort --------")
arr = [42, 89, 17, 56, 33, 10, 91]
print(merge_sort(arr))

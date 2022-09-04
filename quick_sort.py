def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    grater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(grater)


print(quick_sort([10, 5, 2, 3]))

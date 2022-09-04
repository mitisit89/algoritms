def sum(arr: list) -> int:
    if not len(arr):
        return 0 
    return arr[0] + sum(arr[1:])


print(sum([1, 2, 3, 4, 5]))

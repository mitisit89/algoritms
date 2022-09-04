def conuntdown(i: int) -> int | None:
    print(i)
    if i <= 0:
        return None
    return conuntdown(i - 1)


conuntdown(20)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print("factorial")
print(factorial(19))


def sum(arr: list) -> int:
    if not len(arr):
        return 0
    return arr[0] + sum(arr[1:])


print(sum([1, 2, 3, 4, 5]))

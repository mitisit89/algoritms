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

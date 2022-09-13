voted: dict = {}


def check_voter(name: str) -> str:
    if voted.get(name):
        return f"kick them out {name}"
    voted[name] = True
    return f"let them vote {name}!"


print(check_voter("tom"))
print(check_voter("mike"))
print(check_voter("mike"))

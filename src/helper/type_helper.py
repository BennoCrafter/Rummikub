from typing import Any


def args_to_right_type(
    inp: list[str], wanted_types: list[type]
) -> tuple[bool, list[Any]]:
    """
    Converts a list of strings to a list of the wanted types.
    """
    new: list[Any] = []
    for i, z in zip(inp, wanted_types):
        if z is int:
            if not i.replace("-", "").isdigit():
                return False, new
            new.append(int(i))
        else:
            new.append(i)
    return True, new


if __name__ == "__main__":
    args = ["0", "R3", "2"]
    n = [int, str, int]
    n2 = [int, str, str]
    print(args_to_right_type(args, n))
    print(args_to_right_type(args, n2))

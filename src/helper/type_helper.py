def is_convertable(inp: str, wanted_type: type) -> bool:
    if isinstance(wanted_type, int):
        return inp.isdigit()
    return False


def args_to_right_type_auto(inp: list[str]) -> tuple[bool, list]:
    n = []
    for arg in inp:
        if arg.isdigit():
            n.append(int(arg))
        else:
            n.append(str(arg))
    return True, n


def args_to_right_type(inp: list[str], wanted_types: list[type]) -> tuple[bool, list]:
    new = []
    for i, z in zip(inp, wanted_types):
        if z == int:
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
    # print(args_to_right_type_auto(args))
    print(args_to_right_type(args, n))
    print(args_to_right_type(args, n2))

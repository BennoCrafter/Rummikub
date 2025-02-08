COLOR_TO_ABRV : dict[str, str] = {
    "red": "R",
    "green": "G",
    "yellow": "Y",
    "blue": "B",
    "joker": "J"
}

# swap key and value of COLOR_TO_ABRV
ABRV_TO_COLOR : dict[str, str] = {v: k for k, v in COLOR_TO_ABRV.items()}

COLOR_CODES: dict[str, str] = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "joker": "\033[35m",
    "reset": "\033[0m"
}

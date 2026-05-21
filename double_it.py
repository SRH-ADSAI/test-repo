"""A module for print-out stuff doubled"""


def double_int(x: int | float | str |
               list[int | float | str]) -> None:
    """This is a Docstring"""

    return x + x


if __name__ == "__main__":
    double_int(2)
    print("This is a module not a main module")

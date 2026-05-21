"""This module for blablabla"""

import double_it    # first way to import

# from double_it import double_it

X_INIT: int = 1


def prod_integers(old_inventory: int, new_inventory: int
                  ) -> int:
    """This is the main function

    :param old_inventory: old sum
    :type old_inventory: int
    :param new_inventory: new sum
    :type new_inventory: int
    :return: the new total inventory
    :rtype: int
    """

    y = old_inventory + new_inventory + X_INIT

    result = double_it.double_int(y)

    return result


if __name__ == "__main__":
    print(prod_integers(1, 2))

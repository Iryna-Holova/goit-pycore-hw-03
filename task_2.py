"""Task 2: Lottery ticket"""

import random


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    """
    Generate a set of unique random numbers within the specified range.

    Args:
        min_number (int): The minimum value of the range (inclusive).
        max_number (int): The maximum value of the range (inclusive).
        quantity (int): The number of unique random numbers to generate.

    Returns:
        list: A sorted list of unique random numbers within the specified
              range. An empty list is returned if the input parameters are
              invalid.
    """
    if min_num < 1 or max_num > 1000 or quantity < 1 or min_num > max_num:
        return []
    if quantity > (max_num - min_num + 1):
        return []
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_num, max_num))
    return sorted(list(numbers))

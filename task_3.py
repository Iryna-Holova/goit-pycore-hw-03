"""Task 3: Phone number normalization"""

import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalize phone number to standard format.

    Args:
        phone_number (str): Phone number in any format.

    Returns:
        str: Phone number in standard format.
    """
    phone_number = re.sub(r'[^0-9,+]', '', phone_number)

    return '+38'[:13-len(phone_number)] + phone_number

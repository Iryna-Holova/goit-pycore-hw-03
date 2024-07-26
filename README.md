# Python Task Solutions

This repository contains solutions for four Python tasks. Each task is implemented in a separate file and addresses a different problem. Below, you will find a brief description of each task and the corresponding solution.

## Task 1: Date Difference

[**File:** `task_1.py`](./task_1.py)

### Description

Create a function `get_days_from_today(date)` that calculates the number of days between the given date and today's date.

### Requirements

- The function takes one parameter: `date` (a string representing the date in 'YYYY-MM-DD' format).
- The function returns an integer indicating the number of days between the given date and today's date. If the date is in the future, the result should be negative.
- If the date format is incorrect, the function returns `None`.

### Solution

The solution uses the `datetime` module to parse the date and calculate the difference in days.

### Example

```python
days = get_days_from_today("2023-10-09")
print(days)  # Outputs the number of days between today and October 9, 2023
```

## Task 2: Lottery Ticket

[**File:** `task_2.py`](./task_2.py)

### Description

Create a function `get_numbers_ticket(min_num, max_num, quantity)` that generates a set of unique random numbers within the specified range.

### Requirements

The function takes three parameters: `min_num` (minimum value), `max_num` (maximum value), and `quantity` (number of unique random numbers to generate).
The function returns a sorted list of unique random numbers within the specified range. If the input parameters are invalid, it returns an empty list.

### Solution

The solution uses the `random` module and `set` to generate unique random numbers and ensure they are within the specified range.

### Example

```python
numbers = get_numbers_ticket(1, 49, 6)
print(numbers) # Outputs a list of 6 unique random numbers between 1 and 49
```

## Task 3: Phone Number Normalization

[**File:** `task_3.py`](./task_3.py)

### Description

Create a function `normalize_phone(phone_number)` that normalizes phone numbers to a standard format.

### Requirements

The function takes one parameter: `phone_number` (a string representing the phone number in any format).
The function removes all non-numeric characters.
If the international code is missing, the function adds `+38` (for Ukraine).

### Solution

The solution uses the `re` module to clean up the phone number and ensure it is in the correct format.

### Example

```python
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized numbers:", sanitized_numbers)
```

Output:

```bash
Normalized numbers: ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
```

## Task 4: Upcoming Birthdays

[**File:** `task_4.py`](./task_4.py)

### Description

Create a function `get_upcoming_birthdays(users)` that helps determine which colleagues need to be congratulated for their birthdays within the next 7 days, including today.

### Requirements

The function takes one parameter: `users` (a list of dictionaries with keys `name` and `birthday` in 'YYYY.MM.DD' format).
The function returns a list of dictionaries with keys `name` and `congratulation_date`, indicating the date to congratulate the user. If the birthday falls on a weekend, the congratulation date is moved to the next Monday.

### Solution

The solution uses the `datetime` module to calculate upcoming birthdays and adjusts for weekends.

### Example

```python
users = [
    {"name": "John Doe", "birthday": "1985.07.16"},
    {"name": "Jane Smith", "birthday": "1990.07.20"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)
```

Output for 2024.07.16

```bash
[{'name': 'John Doe', 'congratulation_date': '2024.07.16'}, {'name': 'Jane Smith', 'congratulation_date': '2024.07.22'}]
```

## Running the Scripts

To run any of the scripts, simply execute them with Python:

```bash
python task_1.py
python task_2.py
python task_3.py
python task_4.py
```

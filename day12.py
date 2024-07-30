#task1
def string_to_integer_with_fallback(input_string, default_value):
    try:
        return int(input_string)
    except ValueError:
        return default_value

#task2
def integer_to_string_with_formatting(number, format_specifier):
    return format(number, format_specifier)

#task3
import math

def float_to_integer_with_rounding(float_number, strategy):
    if strategy == "up":
        return math.ceil(float_number)
    elif strategy == "down":
        return math.floor(float_number)
    elif strategy == "nearest":
        return round(float_number)
    else:
        raise ValueError("Invalid rounding strategy")

#task4
def list_of_strings_to_integers_with_logging(string_list):
    integers = []
    errors = []
    for s in string_list:
        try:
            integers.append(int(s))
        except ValueError:
            errors.append(s)
    return integers, errors


#task5
def add_numbers_enforcing_type(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")
    return a + b

#task6
def cumulative_subtraction(number_list):
    if len(number_list) < 2 or not all(isinstance(x, (int, float)) for x in number_list):
        raise ValueError("List must contain at least two numeric values")
    result = number_list[0]
    for number in number_list[1:]:
        result -= number
    return result

#task7
def exponentiation_table(base, exponent_range):
    return [f"{base}^{i} = {base ** i}" for i in range(1, exponent_range + 1)]

#task8
class DivisionByZeroError(Exception):
    pass

def safe_division(numerator, denominator, precision):
    if denominator == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    return round(numerator / denominator, precision)



#task9
def advanced_string_split_and_conditional_join(input_string, first_delimiter, second_delimiter):
    split_strings = input_string.split(first_delimiter)
    filtered_strings = [s for s in split_strings if len(s) > 3]
    return second_delimiter.join(filtered_strings)


#task10
import re
from collections import Counter

def enhanced_palindrome_check_and_frequency_analysis(input_string):
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', input_string).lower()
    is_palindrome = cleaned_string == cleaned_string[::-1]
    char_frequency = Counter(cleaned_string)
    return is_palindrome, char_frequency


































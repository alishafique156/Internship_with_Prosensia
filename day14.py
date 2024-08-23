#task1
def complex_operations(complex_str, another_complex):
    try:
        complex_num = complex(complex_str)
    except ValueError:
        raise ValueError("Invalid complex number format")

    return (
        complex_num + another_complex,
        complex_num - another_complex,
        complex_num * another_complex,
        complex_num / another_complex
    )

# Example usage
result = complex_operations("3+4j", complex(1, 2))
print(result)

#task2
def binary_to_integer_and_back(binary_str, fixed_length=8):
    integer_value = int(binary_str, 2)
    binary_str_fixed = format(integer_value, f'0{fixed_length}b')
    return integer_value, binary_str_fixed

result = binary_to_integer_and_back("1010", 8)
print(result)

#task3
import json

def dict_to_json_and_back(dictionary):
    try:
        json_str = json.dumps(dictionary)
        dict_from_json = json.loads(json_str)
    except (TypeError, json.JSONDecodeError) as e:
        return dictionary, str(e)
    
    return json_str, dict_from_json

result = dict_to_json_and_back({"name": "Alice", "age": 30})
print(result)

#task4
class DimensionError(Exception):
    pass

def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise DimensionError("Matrices must have the same dimensions")
    
    return [
        [elem1 + elem2 for elem1, elem2 in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = matrix_addition(matrix1, matrix2)
print(result)

#task5
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    cumulative_product = 1
    for factor in factors:
        cumulative_product *= factor
    return factors, cumulative_product

result = prime_factors(100)
print(result)

#task6
def format_string(template, values):
    for key, value in values.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))
    return template

template = "Hello, {name}. You are {age} years old."
values = {"name": "Alice", "age": 30}
result = format_string(template, values)
print(result)

#task7
import re
from collections import Counter

def anagram_check_and_frequency_analysis(str1, str2):
    def clean_string(s):
        return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    cleaned_str1 = clean_string(str1)
    cleaned_str2 = clean_string(str2)
    
    is_anagram = Counter(cleaned_str1) == Counter(cleaned_str2)
    return is_anagram, Counter(cleaned_str1), Counter(cleaned_str2)

result = anagram_check_and_frequency_analysis("listen", "silent")
print(result)

#task8
def flatten(nested_list):
    flat_list = []
    depth = 1
    
    def _flatten(sub_list, current_depth):
        nonlocal depth
        for item in sub_list:
            if isinstance(item, list):
                _flatten(item, current_depth + 1)
                depth = max(depth, current_depth + 1)
            else:
                flat_list.append(item)
    
    _flatten(nested_list, 1)
    return flat_list, depth

nested_list = [[1, 2, [3, 4]], [5, 6], 7]
result = flatten(nested_list)
print(result)

#task9
def pattern_matching(string, pattern):
    if len(string) != len(pattern):
        return False

    for char, pat in zip(string, pattern):
        if pat.isalpha() and not char.isalpha():
            return False
        if pat.isdigit() and not char.isdigit():
            return False

    return True

result = pattern_matching("a1b2", "a1b2")
print(result)

#task10


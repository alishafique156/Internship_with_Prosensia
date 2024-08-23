#task1
def complex_operations(num1, num2):
    try:
        a, b = num1
        c, d = num2

        add_result = (a + c, b + d)
        sub_result = (a - c, b - d)
        mul_result = (a * c - b * d, a * d + b * c)

        if c == 0 and d == 0:
            div_result = "Division by zero error"
        else:
            denom = c**2 + d**2
            real_part = (a * c + b * d) / denom
            imag_part = (b * c - a * d) / denom
            div_result = (real_part, imag_part)

        return {
            "addition": add_result,
            "subtraction": sub_result,
            "multiplication": mul_result,
            "division": div_result
        }

    except TypeError:
        return "Invalid input: Please provide complex numbers as tuples (e.g., (1, 2))"
    except Exception as e:
        return f"An error occurred: {e}"

num1 = (1, 2)
num2 = (3, 4)
result = complex_operations(num1, num2)
print(result)



#task2
def evaluate_polynomial(coefficients, x):
    degree = len(coefficients) - 1
    if degree == 0:
        return coefficients[0]
    elif degree == 1:
        return coefficients[0] * x + coefficients[1]
    elif degree == 2:
        return coefficients[0] * x**2 + coefficients[1] * x + coefficients[2]
    elif degree == 3:
        return coefficients[0] * x**3 + coefficients[1] * x**2 + coefficients[2] * x + coefficients[3]
    else:
        result = 0
        for i, coeff in enumerate(coefficients):
            result += coeff * x**(degree - i)
        return result

coefficients_linear = [2, 3]
coefficients_quadratic = [1, 0, -4]
coefficients_cubic = [1, -3, 3, -1]
coefficients_higher = [1, 0, 0, -4, 0]

x = 2

print(evaluate_polynomial(coefficients_linear, x))
print(evaluate_polynomial(coefficients_quadratic, x))
print(evaluate_polynomial(coefficients_cubic, x))
print(evaluate_polynomial(coefficients_higher, x))




#task3
def fibonacci(n, depth=0, max_depth=50):
    if depth > max_depth:
        phi = (1 + 5 ** 0.5) / 2
        return int(phi**n / 5**0.5 + 0.5)
    if n <= 1:
        return n
    return fibonacci(n - 1, depth + 1, max_depth) + fibonacci(n - 2, depth + 1, max_depth)

n = 10
print(fibonacci(n))

n = 100
print(fibonacci(n))


#task4
def evaluate_polynomial(coefficients, x):
    degree = len(coefficients) - 1
    if degree == 0:
        return coefficients[0]
    elif degree == 1:
        return coefficients[0] * x + coefficients[1]
    elif degree == 2:
        return coefficients[0] * x**2 + coefficients[1] * x + coefficients[2]
    elif degree == 3:
        return coefficients[0] * x**3 + coefficients[1] * x**2 + coefficients[2] * x + coefficients[3]
    else:
        result = 0
        for i, coeff in enumerate(coefficients):
            result += coeff * x**(degree - i)
        return result

coefficients_linear = [2, 3]
coefficients_quadratic = [1, 0, -4]
coefficients_cubic = [1, -3, 3, -1]
coefficients_higher = [1, 0, 0, -4, 0]

x = 2

print(evaluate_polynomial(coefficients_linear, x))
print(evaluate_polynomial(coefficients_quadratic, x))
print(evaluate_polynomial(coefficients_cubic, x))
print(evaluate_polynomial(coefficients_higher, x))

#task5
def prime_generator(limit):
    cache = []
    sieve = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
        p += 1
    for p in range(2, limit + 1):
        if sieve[p]:
            cache.append(p)
            yield p


for prime in prime_generator(100):
    print(prime)



#task6
def fibonacci(n, max_cache_size=1000):
    cache = {}

    def fib_memo(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        result = fib_memo(n - 1) + fib_memo(n - 2)
        if len(cache) < max_cache_size:
            cache[n] = result
        return result

    def fib_iter(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    if n < max_cache_size:
        return fib_memo(n)
    else:
        return fib_iter(n)


print(fibonacci(10))  
print(fibonacci(10000))  
#task7
import re
from datetime import datetime

def extract_dates(text):
    date_pattern = r'\b(\d{4})[^\d](\d{2})[^\d](\d{2})\b'
    potential_dates = re.findall(date_pattern, text)
    valid_dates = []

    for year, month, day in potential_dates:
        try:
        
            date_str = f"{year}-{month}-{day}"
            datetime.strptime(date_str, "%Y-%m-%d")
            valid_dates.append(date_str)
        except ValueError:
            continue  

    return valid_dates


text = "Here are some dates: 2024-07-24, 2023/05/15, 2022.11.30, and an invalid date 2023-02-30."
print(extract_dates(text))

#task8
import re

def digit_to_word(digit):
    return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][int(digit)]

def transform_string(text):
    text = re.sub(r'\d', lambda x: digit_to_word(x.group()), text)
    
    words = text.split()

    # Transform each word
    transformed_words = []
    for word in words:
        if len(word) > 5:
            word = word[::-1]
        transformed_words.append(word)
    transformed_text = ' '.join(transformed_words).title()

    return transformed_text

text = "This is a sample text with digits 12345 and words longer than five characters."
print(transform_string(text))

#task9
import re

def evaluate_expression(expression, variables):
    def variable_substitution(match):
        var = match.group(0)
        if var in variables:
            return str(variables[var])
        else:
            raise ValueError(f"Undefined variable: {var}")

    expression = re.sub(r'\b\w+\b', variable_substitution, expression)
    try:
        result = eval(expression)
    except (NameError, SyntaxError):
        raise ValueError("Invalid expression")
    
    return result
variables = {'x': 10, 'y': 5}
expression = "x + y * 2"
print(evaluate_expression(expression, variables))

#task10
import re
from datetime import datetime

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_entries(entries):
    report = []

    for entry in entries:
        result = {'entry': entry}
        
        if 5 <= len(entry) <= 20:
            result['length'] = 'Pass'
        else:
            result['length'] = 'Fail'

        if entry.isalpha():
            result['content'] = 'Alphabetic'
        elif entry.isdigit():
            result['content'] = 'Numeric'
        elif entry.isalnum():
            result['content'] = 'Alphanumeric'
        else:
            result['content'] = 'Other'

        if is_valid_email(entry):
            result['format'] = 'Email'
        elif is_valid_date(entry):
            result['format'] = 'Date'
        else:
            result['format'] = 'None'

        report.append(result)
    
    return report

entries = [
    "example@example.com",
    "2024-08-02",
    "123456",
    "HelloWorld",
    "short",
    "this_is_a_very_long_entry"
]

validation_report = validate_entries(entries)
for entry in validation_report:
    print(entry)



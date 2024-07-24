#task1
def print_greeting():
    print("Hello, World!")
print_greeting()

#task2
def max_value(s):
    return max(s)
result = max_value("Hello World")
print(result)

#task3
def convert_to_float(n):
    return float(n)
result = convert_to_float(42)
print(result)

#task4
def add_numbers(a, b):
    return a + b
result = add_numbers(10, 20)
print(result)

#task5
def greet(language_code):
    greetings = {
        'en': "Hello",
        'es': "Hola",
        'fr': "Bonjour"
    }
    print(greetings.get(language_code, "Hello"))
greet('en')
greet('es')
greet('fr')

#task6
def compute_pay(hours_worked, hourly_rate):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_pay = 40 * hourly_rate
        overtime_pay = overtime_hours * (hourly_rate * 1.5)
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours_worked * hourly_rate
    return gross_pay
pay = compute_pay(45, 10)
print(pay)

#task7
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
print(is_integer("123"))
print(is_integer("hello"))

#task8
def print_lyrics():
    print("Twinkle, twinkle, little star,")
    print("How I wonder what you are!")
    print("Up above the world so high,")
    print("Like a diamond in the sky.")
print_lyrics()

#task9
def multiply_numbers(a, b):
    return a * b
result = multiply_numbers(7, 8)
print(result)

#task10
def calculate_expression():
    return 1 + 2 * float(3) / 4 - 5
result = calculate_expression()
print(result)






















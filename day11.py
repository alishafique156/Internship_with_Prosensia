#task1
def string_to_integer(s):
    try:
        return int(s)
    except ValueError:
        return None
print(string_to_integer("123"))  
print(string_to_integer("abc"))  

#task2
def integer_to_string(n):
    return str(n)

print(integer_to_string(123))  

#task3
def float_to_integer(f):
    return int(f)
print(float_to_integer(123.45))  

#task4
def list_of_strings_to_integers(lst):
    return [int(x) for x in lst if x.isdigit()]

print(list_of_strings_to_integers(["123", "abc", "456"]))  

#task5
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(3, 5))  

#task6
def subtract_two_numbers(a, b):
    return a - b

print(subtract_two_numbers(10, 4))  

#task7
def multiply_two_numbers(a, b):
    return a * b
print(multiply_two_numbers(3, 5))  

#task8
def divide_two_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print(divide_two_numbers(10, 2))  
print(divide_two_numbers(10, 0))  

#task9
def concatenate_two_strings(s1, s2):
    return s1 + s2
print(concatenate_two_strings("Hello, ", "World!")) 

#task10
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello"))  












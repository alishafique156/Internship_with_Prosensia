#task1
# Calculate the gross pay
print(" This program will calculate the Grass Pay ")
hours = input('How many hours you worked?')
HOURS=int(hours)
hourly_wage=input(' How much you earn per hours?')
wage=float(hourly_wage)
pay=HOURS*wage
print (pay)

#task2
#Temperature Conversion 
temp=input('Enter a temperature in celsius?')
Temp=int(temp);
TEMP=(Temp*9/5)+32
print (TEMP)

#task3
#Number Sign Check 
number = float(input("Please enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
 print("The number is zero.")
 
 
 #task4
 #Leap Year Checker
year = int(input("Please enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#task5
#Basic Arithmetic Operations 

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

sum_result = number1 + number2
difference = number1 - number2
product = number1 * number2

if number2 != 0:
    quotient = number1 / number2
else:
    quotient = "undefined (division by zero)"
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")


#task6
#Calculate Factorial 
number = int(input("Enter a number: "))
factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, number + 1):
        factorial *= i
print(f"The factorial of {number} is {factorial}")

#task7
#Reverse a String 
user_input = input("Please enter a string: ")
reversed_string = ""

for i in range(len(user_input) - 1, -1, -1):
    reversed_string += user_input[i]

print("The reversed string is:", reversed_string)

#task7
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
    if ival > 0:
        print('Nice work')
    else:
        print('The number is not positive')
except ValueError:
    print('Not a number')


#task8
#Multiply Two Numbers 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 * num2
print("The result of multiplying", num1, "and", num2, "is:", result)

#task9
#Square of a Number 
number = float(input("Enter a number: "))
square = number * number
print("The square of", number, "is:", square)

#task10
#Divide Two Numbers
number = int(input("Enter a number: "))
factorial = 1
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, number + 1):
        factorial *= i
print(f"The factorial of {number} is {factorial}")
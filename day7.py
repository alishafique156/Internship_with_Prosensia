#task1
number = int(input("Please enter an integer: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
    
#task2

x=5
if x<2:
    print('Number is too small')
    print('Still Smaller')
    print('Done with 2')

#task3
x=5
if x>2:
    print('Bigger than 2')
    print('Still bigger')
    print('Done with 2')
    
#task4

number = int(input(" Enter an integer: "))
if 10 <= number <= 20:
    print("Within range")
else:
    print("Out of range")

#task5
x= int(input(" Enter a number: "))
if x==2:
    print("Equal")
else:
    print('Not Equal') 
    print('all done')
    
#task6
x = int(input(" Enter a number: "))
if x<10:
    print('Small')
elif 10>=x<=20:
    print('Medium')
elif x>20:
    print('Greater')   
else:
    print('Something else')
    print('All done')  

#task8
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_pay = 40 * hourly_rate
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * hourly_rate
    print(f"Gross pay: ${gross_pay:.2f}")


#task9
# Ask the user to input two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
if num1 > 0 and num2 > 0:
    print("Both are positive")
elif num1 > 0 or num2 > 0:
    print("One is positive")
else:
    print("None are positive")

#task10
number = int(input("Enter a number: "))
if number > 0:
    if number % 2 == 0:
        print("Positive and even")
    else:
        print("Positive but odd")
else:
    print("Negative")



    
    
#task1
numbers = []
while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Sum: {total}, Average: {average}")
else:
    print("No numbers were entered.")

#task2
numbers = [3, 7, 1, 12, 9, 5]
threshold = 6
filtered_numbers = [num for num in numbers if num > threshold]
print(f"Numbers greater than {threshold}: {filtered_numbers}")

#task3
numbers = [int(num) for num in input("Enter a list of numbers separated by spaces: ").split()]
largest = smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

for num in numbers:
    if num < smallest:
        smallest = num

print(f"Largest number: {largest}, Smallest number: {smallest}")


#task4
numbers = [3, 7, 3, 12, 9, 7, 5]
unique_numbers = list(set(numbers))
print(f"List without duplicates: {unique_numbers}")

#task5
while True:
    line = input("Enter text (or 'done' to finish): ")
    if line.lower() == 'done':
        break
    if line.startswith('#'):
        continue
    print(line)

#task6
predefined_number = 42
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess == predefined_number:
        print("Correct! You guessed the number.")
        break
    else:
        print("Wrong guess. Try again.")

if attempts == max_attempts:
    print("You've reached the maximum number of attempts.")

#task7
N = int(input("Enter a number: "))
sum_of_squares = sum(i**2 for i in range(1, N+1))
print(f"Sum of squares of the first {N} natural numbers is: {sum_of_squares}")

#task8
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(f"Reversed string: {reversed_string}")

#task9
N = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = [0, 1]

for i in range(2, N):
    next_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)

print(f"The first {N} numbers in the Fibonacci sequence are: {fib_sequence[:N]}")
























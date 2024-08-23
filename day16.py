#task1
file = open("data.txt", "r")
file.close()
#task2
file = open("data.txt", "r")
content = file.readlines()
for line in content:
    print(line.strip())
file.close()

#task3
file = open("output.txt", "w")
file.write("Hello, World!")
file.close()

#task4
try:
    file = open("data.txt", "r")
    file.close()
except FileNotFoundError:
    print("The file data.txt does not exist.")

#task5
file = open("data.txt", "r")
line_count = len(file.readlines())
print("Number of lines:", line_count)
file.close()

#task6
file = open("log.txt", "r")
lines = file.readlines()
for line in lines:
    if "error" in line:
        print(line.strip())
file.close()

#task7
with open("data.txt", "r") as src:
    with open("data_copy.txt", "w") as dst:
        dst.write(src.read())

#task8
with open("output.txt", "a") as file:
    file.write("End of file")

#task9
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

#task10
import os
file_size = os.path.getsize("data.txt")
print("Size of data.txt in bytes:", file_size)

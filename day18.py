#task1
my_dict = {}
my_dict['key1'] = 'value1'
my_dict['key2'] = 'value2'
my_dict['key3'] = 'value3'
print(my_dict)


#task2
def print_value(dictionary, key):
    if key in dictionary:
        print(dictionary[key])
    else:
        print(f"Key '{key}' not found.")

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print_value(my_dict, 'key2')
print_value(my_dict, 'key4')

#task3
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print("Before update:", my_dict)
my_dict['key2'] = 'updated_value2'
print("After update:", my_dict)

#task4
text = input("Enter a line of text: ")
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

#task5
def print_keys_and_values(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    print("Keys:", keys)
    print("Values:", values)

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print_keys_and_values(my_dict)


#task6
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
value = my_dict.get('key4', 0)
print(value)


#task7
students = {
    'student1': {
        'name': 'Alice',
        'age': 20,
        'grades': {
            'math': 'A',
            'science': 'B+'
        }
    },
    'student2': {
        'name': 'Bob',
        'age': 21,
        'grades': {
            'math': 'B',
            'science': 'A'
        }
    }
}

print(students)


#task8
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'd': 4, 'e': 5}
result = merge_dicts(dict1, dict2)
print(result)

#task9

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
try:
    print(my_dict['key4'])
except KeyError:
    print("Custom error message: Key 'key4' not found.")


#task10
def find_most_common_word(filename):
    with open(filename, 'r') as file:
        text = file.read()

    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_common_word = max(word_count, key=word_count.get)
    print(f"The most common word is '{most_common_word}' with {word_count[most_common_word]} occurrences.")

# Example usage:
# find_most_common_word('example.txt')


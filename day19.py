#task1
names = ('Alice', 'Bob', 'Charlie')
print(names[1])

#task2
def max_in_tuple(t):
    return max(t)

print(max_in_tuple((4, 7, 1)))

#task3
t = ('apple', 'banana', 'cherry')
try:
    t[1] = 'orange'
except TypeError:
    print("Cannot modify tuple elements")

#task4
lst = [1, 2, 3]
t = (1, 2, 3)

lst.append(4)
try:
    t.append(4)
except AttributeError:
    print("Cannot use append on tuple")

#task5
def swap(a, b):
    a, b = b, a
    return a, b

a = 5
b = 10
a, b = swap(a, b)
print(a, b)

#task6
def dict_to_tuples(d):
    return list(d.items())

d = {'x': 1, 'y': 2, 'z': 3}
print(dict_to_tuples(d))

#task7
def sort_dict_by_value(d):
    return sorted(d.items(), key=lambda item: item[1], reverse=True)

d = {'a': 10, 'b': 1, 'c': 22}
print(sort_dict_by_value(d))

#task8
def compare_tuples(t1, t2):
    return [a == b for a, b in zip(t1, t2)]

t1 = (1, 2, 3)
t2 = (3, 2, 1)
print(compare_tuples(t1, t2))

#task9
from collections import Counter

def top_n_words(filename, N):
    with open(filename) as f:
        words = f.read().split()
    return Counter(words).most_common(N)

print(top_n_words('romeo.txt', 3))

#task10
def reverse_and_sort_dict(d):
    return sorted([(v, k) for k, v in d.items()])

d = {'a': 10, 'b': 1, 'c': 22}
print(reverse_and_sort_dict(d))


#task1
def concatenate_and_convert(str1, str2):
    concatenated = str1 + str2
    if concatenated.isdigit():
        return int(concatenated)
    return concatenated

#task2
def character_at_index(s, index):
    if index < 0 or index >= len(s):
        return "Index out of bounds"
    return s[index]

#task3
def lengths_of_strings(lst):
    return [len(s) for s in lst]

#task4
def print_characters_with_index(s):
    for i in range(len(s)):
        print(f"Index {i}: {s[i]}")

#task5
def count_character(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count


#task6
def substring(s, start, end):
    if start < 0:
        start = 0
    if end > len(s):
        end = len(s)
    return s[start:end]


#task7
def compare_strings(str1, str2):
    if str1 < str2:
        return "First string comes before the second string"
    elif str1 > str2:
        return "First string comes after the second string"
    else:
        return "Both strings are equal"

#task8
def string_methods(s):
    return {
        "lowercase": s.lower(),
        "uppercase": s.upper(),
        "titlecase": s.title()
    }


#task9
def search_and_replace(s, search_term, replacement_term):
    return s.replace(search_term, replacement_term)


#task10
def remove_whitespace(s):
    return ' '.join(s.split())

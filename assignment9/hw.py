"""
Exercise-1: Find missing elements
Write a function "missing_elements(my_list: list) -> list" that takes a
sorted list of integers and returns a list of missing integers in the range of the list.

Example:
missing_elements([1, 2, 4, 6, 7]) -> [3, 5]
"""
from types import NoneType


def missing_elements(my_list: list) -> list:
    if not my_list:
        return []

    my_list.sort()
    l = []

    if my_list[0] != 1:
        l.append(1)

    for i in range(1, len(my_list)):
        if my_list[i] - my_list[i - 1] > 1:
            l.extend(range(my_list[i - 1] + 1, my_list[i]))

    return l
    pass

"""
Exercise-2: Count occurrences
Write a function "count_occurrences(my_list: list) -> dict" that takes a
list of integers and returns a dictionary where keys are unique integers
from the list and values are their counts in the list.

Example:
count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]) -> {1: 2, 2: 2, 3: 1, 4: 2, 5: 1}
"""

def count_occurrences(my_list: list) -> dict:
    my_list.sort()
    dc = {}

    for z in my_list:
        if z in dc:
            dc[z] += 1
        else:
            dc[z] = 1

    return dc
    pass


"""
Exercise-4: Common elements
Write a function "common_elements(list1: list, list2: list) -> list" that takes two
lists of integers and returns a list of unique common elements.

Example:
common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [3, 4, 5]
"""

def common_elements(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))
    pass

"""
Exercise-5: Character frequency
Write a function "char_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each character in the string.

Example:
char_frequency('hello world') -> {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
"""

def char_frequency(my_string: str) -> dict:
    dc = {}

    for z in my_string:
        if z in dc:
            dc[z] += 1
        else:
            dc[z] = 1

    return dc
    pass

"""
Exercise-6: Unique words
Write a function "unique_words(my_string: str) -> int" that takes a
string and returns the number of unique words in the string.

Example:
unique_words('hello world hello') -> 2
"""

def unique_words(my_string: str) -> int:
    words = my_string.split()

    dc = {}

    for z in words:
        if z not in dc:
            dc[z] = 1

    return len(dc)
    pass

"""
Exercise-7: Word frequency
Write a function "word_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each word in the string.

Example:
word_frequency('hello world hello') -> {'hello': 2, 'world': 1}
"""

def word_frequency(my_string: str) -> dict:
    words = my_string.split()

    dc = {}

    for z in words:
        if z in dc:
            dc[z] += 1
        else:
            dc[z] = 1

    return dc
    pass

"""
Exercise-8: Count elements in range
Write a function "count_in_range(my_list: list, start: int, end: int) -> int" that
takes a list of integers and two integers as range boundaries and
returns the count of unique elements within that range in the list.

Example:
count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4) -> 3
"""

def count_in_range(my_list: list, start: int, end: int) -> int:
    count = 0
    ind = len(my_list)

    for i, z in enumerate(my_list):
        if z == start:
            ind = i
            break

    for i, z in enumerate(my_list):
        if i >= ind:
            count += 1

        if z == end:
            break

    return count
    pass

"""
Exercise-9: Swap dictionary keys and values
Write a function "swap_dict(d: dict) -> dict" that takes a dictionary
and returns a new dictionary where keys become values and values become keys.
if you face duplicates, the first key should be saved.

Example:
swap_dict({1: 'a', 2: 'b', 3: 'c'}) -> {'a': 1, 'b': 2, 'c': 3}
"""

def swap_dict(d: dict) -> dict:
    dc = {}

    for k, v in d.items():
        if v not in dc:
            dc[v] = k

    return dc
    pass

"""
Exercise-10: Subset check
Write a function "is_subset(set1: set, set2: set) -> bool" that takes two
sets and returns True if set2 is a subset of set1, and False otherwise.

Example:
is_subset({1, 2, 3, 4, 5}, {3, 4, 5}) -> True
"""

def is_subset(set1: set, set2: set) -> bool:
    return set2.issubset(set1)
    pass

"""
Exercise-11: Intersection of lists
Write a function "list_intersection(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in both lists.

Example:
list_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [3, 4, 5]
"""

def list_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))
    pass

"""
Exercise-12: Union of lists
Write a function "list_union(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in either of the lists.

Example:
list_union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [1, 2, 3, 4, 5, 6, 7]
"""

def list_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))
    pass

"""
Exercise-13: Most frequent element
Write a function "most_frequent(my_list: list) -> int" that takes a
list of integers and returns the most frequent element in the list.

Example:
most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 1
"""

def most_frequent(my_list: list) -> int:
    dc = {}

    for z in my_list:
        if z in dc:
            dc[z] += 1
        else:
            dc[z] = 1

    mx = 0
    ans = None

    for i, v in dc.items():
        if v > mx:
            mx = v
            ans = i

    return ans
    pass

"""
Exercise-14: Least frequent element
Write a function "least_frequent(my_list: list) -> int" that takes a
list of integers and returns the least frequent element in the list.

Example:
least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 3
"""

def least_frequent(my_list: list) -> int:
    dc = {}

    for z in my_list:
        if z in dc:
            dc[z] += 1
        else:
            dc[z] = 1

    mn = len(my_list) + 1
    ans = None

    for i, v in dc.items():
        if v < mn:
            mn = v
            ans = i

    return ans
    pass


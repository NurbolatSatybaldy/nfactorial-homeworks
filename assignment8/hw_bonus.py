"""
💎 Exercise-1 (Longest Consecutive Sequence):
Write a function "longest_consecutive(my_list: list[int]) -> int" that takes a 
list of integers and returns the length of the longest consecutive elements 
sequence in the list. The list might be unsorted.

Example:

longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""

def longest_consecutive(my_list: list[int]) -> int:

    count = 1

    my_list = sorted(my_list)

    for i, j in enumerate(my_list):
        if i + 1 < len(my_list) and my_list[i + 1] == my_list[i] + 1:
            count += 1

    return count if count != 1 else 0
    pass

"""
💎 Exercise-2 (Find missing number):
Write a function "find_missing(my_list: list[int]) -> int" that takes a 
list of integers from 1 to n. The list can be unsorted and have one 
number missing. The function should return the missing number.

Example:

find_missing([1, 2, 4]) -> 3
"""

def find_missing(my_list: list[int]) -> int:
    my_list = sorted(my_list)

    num = None

    for i, j in enumerate(my_list):
        if my_list[0] != 1:
            num = 1
            break
        if i + 1 < len(my_list) and my_list[i + 1] != my_list[i] + 1:
            num = my_list[i] + 1

    return num
    pass


"""
💎 Exercise-3 (Find duplicate number):
Write a function "find_duplicate(my_list: list[int]) -> int" that takes a list 
of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

Example:

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""

def find_duplicate(my_list: list[int]) -> int:
    dc = {}
    ans = None

    for z in my_list:
      if z in dc:
          dc[z] += 1
      else:
          dc[z] = 1

    for k,v in dc.items():
        if v > 1:
            ans = k

    return ans
    pass


"""
💎 Exercise-4 (Group Anagrams):
Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

def group_anagrams(words: list[str]) -> list[list[str]]:
    dc = {}

    for z in words:
        s = tuple(sorted(z))
        if s in dc:
            dc[s].append(z)
        else:
            dc[s] = [z]

    new_list = []
    for z in dc.values():
          new_list.append(z)

    return new_list
    pass

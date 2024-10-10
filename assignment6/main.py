def task1():
    a = 3
    b = 4
    print(a + b)

def task2():
    some_string = 'Whatsup'
    another_string = some_string[::-1]
    print(another_string)

def task3():
    some_string = 'Something'
    print(len(some_string))

def task4():
    string1 = "hi"
    string2 = 'hello'
    print(string1 + string2)

def task5():
    char = 'a'
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    print(char in vowels)

def task6():
    some = "GreatestMovie"
    some1 = some[len(some) - 1] + some[1:len(some) - 1] + some[0]
    print(some1)

def task7():
    some = "jackson"
    print(some.upper())

def task8():
    a = 8
    b = 7
    area = 8 * 7
    print(area)

def task9():
    a = 47
    print(bool(a % 2 == 0))

def task10():
    a = 'heyheyhey'
    print(a[:3])

def task11():
    name = 'Nicolas'
    surname = 'Jackson'
    print(f'{name} {surname}')

def task12():
    some = 'Something'
    print(some[2:6])

def task13():
    some = '156'
    print(int(some))

def task14():
    some = 'ooooop'
    some = some * 3
    print(some)

def task15():
    a = 57
    b = 6

    q = 57 // 6
    r = 57 % 6

    print(f'quotient:{q} and r:{r}')

def task16():
    a = 57
    b = 6
    print(f'divsion:{a/b}')

def task17():
    some = "Zhanibek"
    print(f"Occurrences of k = {some.count('k')}")

def task18():
    some = "I said \"Let me cook\""
    print(some)

def task19():
    some = """Do I wanna know
if this feeling flows both ways
(Sad to see you go)"""
    print(some)

import math
def task20():
    a = 4
    b = 4
    res = math.pow(a, b)
    print(int(res))

def task21():
    some = "rotator"
    print(str(some == some[::-1]))

def task22():
    some1 = "spar"
    some2 = 'rasp'
    print(str(sorted(some1) == sorted(some2)))

def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
    task11()
    task12()
    task13()
    task14()
    task15()
    task16()
    task17()
    task18()
    task19()
    task20()
    task21()
    task22()

if __name__ == "__main__":
    main()

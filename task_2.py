# Завдання 2

from collections import deque

def check_palindrome(string):
    string = string.lower().replace(' ', '')
    deque_string = deque(string)
    # print(deque_string)
    while len(deque_string) > 1:
        if deque_string.popleft() != deque_string.pop():
            return False
    return True

# Test
string1 = 'Сир і рис'
string2 = '404'
string3 = '4004'
string4 = 'Сіно ніс'
string5 = 'Паліндром'
string6 = 'Паліндром і Морднілап'

print(f'"{string1}" is palindrome: {check_palindrome(string1)}')
print(f'"{string2}" is palindrome: {check_palindrome(string2)}')
print(f'"{string3}" is palindrome: {check_palindrome(string3)}')
print(f'"{string4}" is palindrome: {check_palindrome(string4)}')
print(f'"{string5}" is palindrome: {check_palindrome(string5)}')
print(f'"{string6}" is palindrome: {check_palindrome(string6)}')
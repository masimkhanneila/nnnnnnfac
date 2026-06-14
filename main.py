#1
a = 5
b = 6
def add(x, y):
    return x + y
print(add(a, b))
#2
s = "string"
def reverse_string(s):
    return s[::-1]
print(reverse_string(s))
print(s)
#3
def length_of_string(s):
    return len(s)
print(length_of_string(s))
#4
s2 = "string2"
def concatenate_strings(s1, s2):
    return s1 + s2
print(concatenate_strings(s, s2))
#5
c = 'c'
def is_vowel(c):
    return c in 'aeiouAEIOU'
print(is_vowel(c))
#6
def swap_first_last(s):
    new_s = s[-1] + s[1:-1] + s[0]
    return new_s
print(swap_first_last(s))
#7 
def to_uppercase(s):
    string_toreturn = ""
    for char in s:
        if ord(char) > 90 :
            string_toreturn += chr(ord(char) - 32)
        else:
            string_toreturn += char
    return string_toreturn
print(to_uppercase(s))
#8
length = 5
width = 6
def area_of_rectangle(length, width):
    return length * width
print(area_of_rectangle(length, width))
#9
def is_even(n):
    return n % 2 == 0
print(is_even(length))
#10
def first_three(s):
    return s[:3]
print(first_three(s))
#11
name = "Neila"
age = 18
message = f'My name is {name} and my age is {age}'
print(message)
#12
def char_from_2_to_5(s):
    return s[2:6]
print(name)
#13
n = "5"
def string_to_integer(n):
    return int(n)
print(string_to_integer(n)+1)
#14
school = "nfactorial"
def repeat_string(s,m):
    return s * m
print(repeat_string(school,3))
#15
first_num = 17
second_num = 5
def q_r(x, y):
    return x // y, x % y
print(q_r(first_num, second_num))
#16
def float_division(x, y):
    return x / y
print(float_division(first_num, second_num))
#17
yo = "yoyoyoyoyo"
char = 'y'
def count_char(s,c):
    return s.count(c)
print(count_char(yo,char))
#18
food = "pizza \"Motzarella\" and cola"
print(food)
#19
cola = """
cola 
is
the 
best 
with 
everything
"""
print(cola)
#20
base = 5
exponent = 3
def power(base, exponent):
    return base ** exponent
print(power(base, exponent))
#21
palindrome = "ColaaloC"
def reverse_string(s):
    return s[::-1]
def is_palindrome(s):
    if s == reverse_string(s):
        return True
    else:
        return False
print(is_palindrome(palindrome))
#22
first_word = "listen"
second_word = "silent"
def is_anagram(s1, s2):
    s11 = s1.lower()
    s22 = s2.lower()
    arr1 = []
    for i in range(len(s11)):
        arr1.append(s11[i])
    for i in range(len(s22)):
        if s22[i] in arr1:
            arr1.remove(s22[i])
    return len(arr1) == 0
print(is_anagram(first_word, second_word))
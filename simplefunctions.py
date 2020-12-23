def factorial(number):                  # silnia
    factorial = number
    number = number - 1
    while number > 0:
        factorial = factorial * number 
        number = number -1
    return factorial

def string_rev(str1):                   # odwróć strin
    r_str1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1]
        index = index -1
    return rstr1

def in_range(number, ranged, rangeu):       # czy liczba mieści się w zakresie
    if number in range(ranged, rangeu):
        print(f'{number} is in range')
    else:
        print(f'{number} is out of range')

def count_upandlowletters(str1):            # liczy duże małe literyw stringu
    upp_letters = 0
    low_letters = 0
    for l in str1:
        if l.isupper():
            upp_letters += 1
        elif l.islower():
            low_letters += 1
    return f'{low_letters} lower case letters \n{upp_letters} upper case letters'


print(count_upandlowletters('Dam ianGizA '))
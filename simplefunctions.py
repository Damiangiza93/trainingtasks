def factorial(number):                      # silnia
    factorial = number
    number = number - 1
    while number > 0:
        factorial = factorial * number 
        number = number -1
    return factorial

def string_rev(str1):                       # odwróć strin
    r_str1 = ''
    index = len(str1)
    while index > 0:
        r_str1 += str1[ index - 1]
        index = index -1
    return r_str1

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

def unique_elements_list(list1):            # zwraca tylko unikalne rekordy z listy
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2    

def is_prime(number):                       # sprawdza czy liczba pierwsza
    prime = ''
    if number==1:
        return 'Number is not prime'
    else:
        for i in range(2, number):
            if (number/i) == (number//i):
                prime = 'Number is not prime'
        if prime == '':
            prime = 'Number is prime'
        return prime

def even_nums(list1):                       # zwraca liczby parzyste
    list2 = []
    for n in list1:
        if (n%2) == 0:
            list2.append(n)
    return list2

def isperfect_num(num):                       # sprawdza czy perfect number - numer którego suma dzielników jest równa temu numerowi
    divsum = 0
    for n in range(1,num):
        if (num%n) == 0:
            divsum += n
    if divsum == num:
        print('Number is perfect')
    else:
        print('Number is not perfect')


def ispalindrome(string):
    left = 0
    right = len(string) - 1

    while right >= left:
        if not string[left] == string[right]:
            return False
        left += 1
        right -=1
    return True

def pascal_triangle(rows):
    print('1')
    print('1 1')
    list1 = [1,1]
    for i in range(2,rows):
        list2 = []
        for n in range(0, (len(list1)-1)):
            list2.append(list1[n]+list1[n+1])
            list1.insert(n+1, list2[n])
        print(list1)


        
print(pascal_triangle(4))
#print(ispalindrome('nursesrun'))

# print(perfect_num(496))
# print(even_nums([1,2,3,4,5,6,7]))
# print(is_prime(1))
# print(count_upandlowletters('Dam ianGizA '))
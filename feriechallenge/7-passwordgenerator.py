'''
Napisz program do generowania losowych haseł o zadanej przez użytkownika długości. Hasło musi spełniać zadane warunki np. 
co najmniej jedna liczba, 
co najmniej po jednej dużej i małej literze. Warto skorzystać z modułów string i secrets.

Propozycja rozszerzenia: Po wygenerowaniu hasła skopiuj je do schowka systemowego 🙂
'''

import pyperclip
import string
import secrets

length = int(input('Length of password:'))

''' utworzenie hasła '''
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password)):
        break
print(password)
''' skopiowanie do schowka '''
pyperclip.copy(password)



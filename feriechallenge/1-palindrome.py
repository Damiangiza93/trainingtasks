'''
Check if it is palindrome and show the page with anagrams
'''
def ispalindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    b = ''
    
    for i in range(len(s)):
        b += s[len(s)-1-i]
    print('Reversed:', b)
    
    print('Is it a palindrome:')
    if s == b:
        print(True)
    else:
        print(False)

    url = f'https://poocoo.pl/scrabble-slowa-z-liter/{s}'
    return f'Here you can check anagrams of the word {s}: \n{url}'

print(ispalindrome(input('Write a word: ')))

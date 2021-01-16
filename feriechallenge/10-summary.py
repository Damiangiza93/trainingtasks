'''
Napisz program, który odczytuje wszystkie pliki stworzone przez Ciebie podczas #feriechallenge - przeszukuje lokalne katalogi lub łączy się w tym celu z 
Githubem. Postaraj się jak najmniej hardcodować i na przykład nie podawaj listy wszystkich plików ręcznie 🙂  Następnie wykorzystując swój sposób 
katalogowania programów automat odczytuje i wyświetla takie informacje:
-> do ilu zadań z 10 napisało się kod
-> liczba linijek kodu napisanych w każdym zadaniu (bez uwzględniania pustych!) oraz sumaryczna liczba linijek
-> liczba unikalnych słów użytych we wszystkich programach oraz najczęściej występujące słowo
-> lista i liczba słów kluczowych użyta podczas całego challenge (wykorzystaj moduł keywords)
-> lista i liczba zaimportowanych modułów we wszystkich programach

Propozycja rozszerzenia: Po prostu miej odwagę i pochwal się outputem swojego programu! - opublikuj posta z tagiem #feriechallenge i zostaw lajka na 
naszej stronie, będzie nam miło 🙂 Możesz też oczywiście umieścić jakieś dodatkowe statystyki.
'''

import os
from collections import Counter
from keyword import iskeyword
  
def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0][0] 

def onlyalphaspaces(string):
    line1 = ''
    for i in string:
        if i.isalpha() or i == ' ':
            line1 += i
        else:
            i = ' '
            line1 += i
    return line1

''' liczba wykonanych zadań '''
number_of_tasks = 0
f_list = []
for file in os.listdir('C:/Users/abc/Pro/trainingtasks/feriechallenge'):
    name, ext = file.split('.')
    if ext == 'py':
        f_list.append(file)
        number_of_tasks += 1

print(f'\n{number_of_tasks}/10 tasks made')


all_lines = 0
line_num_list = []
words_list = []
modules_num = 0
modules_list = []
for name in f_list:
    i = 0
    with open(name, 'r', encoding='utf-8') as f:
        for line in f:
            line1 = onlyalphaspaces(line)
            line_words = list(w.lower() for w in line1.split())

            check = False
            if line_words != [] and line_words[0] == 'import':
                modules_num += 1
                modules_list.append(line_words[1])
            elif line_words != [] and line_words[0] == 'from':
                for w in line_words:
                    if check == True:
                        modules_num += 1
                        modules_list.append(f'{w}')
                    if w == 'import':
                        check = True
            else:
                pass

            words_list.extend(line_words)

            if line != '\n':
                i += 1
    all_lines += i
    line_num_list.append({'name': name,'lines_num': i})

keywords_list = []
keywords_num = 0
for w in words_list:
    if iskeyword(w):
        keywords_num += 1
        keywords_list.append(w)

print('\nNumber of lines in each program:')
for program in line_num_list:
    print(f"{program['name']} - {program['lines_num']}" )

print()
print(f'Number of lines in all files: {all_lines}')
print(f'Most frequent word: {most_frequent(words_list)}')
print(f'Unique words number: {len(set(words_list))}')
print(f'Keywords number: {keywords_num}')
print(f'Keywords list: {set(keywords_list)}')
print(f'Number of modules: {modules_num}')
print(f'List of modules: {set(modules_list)}')


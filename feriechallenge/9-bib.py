'''Napisz program, który importuje katalog z dowolnej biblioteki (np. API Biblioteki Narodowej http://data.bn.org.pl/ - przykład użycia: 
http://data.bn.org.pl/api/bibs.json?author=Andrzej+Sapkowski&amp;kind=ksi%C4%85%C5%BCka). Użytkownik może podać autora i program pokaże mu, 
jakie książki tego autora są w zbiorach biblioteki. Następnie daj użytkownikowi możliwość “wypożyczania” i “zwracania” książek - posiadane pozycje są 
składowane w pliku zawierającym pewien identyfikujący zbiór danych, np. tytuł, autor, wydawnictwo, rok wydania (możesz też użyć lokalnej bazy danych), 
w przypadku “wypożyczenia” książki są do niego dodawane, a w przypadku “zwracania” usuwane.

Propozycja rozszerzenia: W prostym przypadku lokalne “wypożyczanie” nie ma wpływu na katalog biblioteki, czyli w teorii można wypożyczyć książkę 
nieskończoną liczbę razy. Zabezpiecz program w taki sposób, aby podczas pobierania danych rozpoznawał też pozycje “wypożyczone” lokalnie i nie pokazywał 
ich już jako wyniki wyszukiwania.
'''
import sqlite3 
import requests
from time import sleep

conn = sqlite3.connect('bib.db')
conn.execute('''CREATE TABLE IF NOT EXISTS books
         (title         TEXT    PRIMARY KEY    NOT NULL,
         author         TEXT        NOT NULL,
         pub_year       INT,
         id             TEXT        NOT NULL);
         ''')

def add_new_book(data):
    sql = f'INSERT INTO books (title,author,pub_year,id) VALUES (?,?,?,?);'
    conn.execute(sql,data) 
    conn.commit()

def checkbyauthor(author):
    url = f"http://data.bn.org.pl/api/bibs.json?author={author};kind=książka;language=polski;boolean=true&amp;limit=100"
    response = requests.request("GET", url).json()['bibs']
    return response

def sort(e):
    return e['publicationYear']

 
check = ''
while check != 'z':
    check = input('Chcesz (w)ypożyczyć książkę, (o)ddać książkę czy (z)akończyć? (w/o/z):')
    print()
    if check == 'w':
        author = input('Podaj autora:')
        books = checkbyauthor(author)
        books.sort(key=sort)

        print('id rok książka\n')
        for i,book in enumerate(books):
            print(f"{i} {book['publicationYear']} {book['title']}")
        print()

        try:
            choosed_book_num = input('Podaj id książki którą chcesz wypożyczyć. Jeśli chcesz wyjść wpisz cokolwiek innego:')
            book = books[int(choosed_book_num)]
            add_new_book([book['title'], book['author'], book['publicationYear'], book['id']])
            print(f"Książka {book['title']} zostala wypożyczona\n")
        except:
            print('Błędna nazwa authora, id książki. Spróbuj jeszcze raz\n')
            pass

    elif check == 'o':
        print('Wypożyczone książki:\n')
        sleep(0.3)
        cursor = conn.execute("SELECT title, author, pub_year, id from books")
        for row in cursor:
            print("Tytuł = ", row[0])
            print("Autor = ", row[1])
            print("Rok publikacji = ", row[2])
            print("ID = ", row[3], "\n")
            sleep(0.3)
        
        book_id = [input('Podaj id książki do oddania:')]
        isin = False
        for i in conn.cursor().execute("SELECT title, id from books").fetchall():
            if book_id[0] == i[1]:
                btitle = i[0]
                isin = True
                break
        if isin:
            conn.execute("DELETE from books where id = ?;", book_id)
            conn.commit()
            print(f'Książka {btitle} została oddana \n')
        else:
            print('Nie posiadasz książki o podanym id. Spróbuj jeszcze raz')
            
    elif check == 'z':
        print('Dziękujemy za skorzystanie z biblioteki')
    else:
        print('Coś robisz źle. Spróbuj jeszcze raz\n')

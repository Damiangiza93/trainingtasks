'''Przy wykorzystaniu API (np. IMDB) wyszukaj wszystkie części filmu zadanego w wyszukiwaniu (np. Rambo, Scary Movie, Shrek). Można przyjąć założenie, 
że wszystkie filmy “z serii” muszą zawierać szukany ciąg - czasem zdarzają się błędne wyniki wyszukiwania z baz, można je spróbować odfiltrować. 
Wyświetl dla każdego podstawowe informacje np. rok, długość, ocena, spis aktorów (pierwszych 5 z listy).
Przykładowe API do wykorzystania: 
https://rapidapi.com/apidojo/api/imdb8/endpoints - do wyszukania filmów z daną nazwą (do odfiltrowania można użyć warunku, że dany rekord posiada nazwę i 
rok wydania)
https://rapidapi.com/.../imdb-internet-movie-database... - pobranie szczegółów o danym filmie
'''

''' wyszukaj wszystkie części '''

import requests

key = "Here write your x-rapidapi-key"

''' znajdz filmy '''
url = "https://imdb8.p.rapidapi.com/title/auto-complete"
fname = input('Name of the movie: ')
querystring = {"q":fname}
headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers, params=querystring)

respdict = response.json()
movieslist = respdict['d']

''' dane o filmie po id '''
def filmdata(filmid):
    url = f'https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{filmid}'
    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers)
    return response.json()


for movie in movieslist:
    movie = dict(movie)
    try:
        if movie['y'] and movie['l'] and movie['s']:
            films = filmdata(str(movie['id']))
            print(films['title'])
            print(films['year'])
            print('Cast:')
            for i in range(5):
                print(films['cast'][i]['actor'])
            print('Length: ',films['length'])
            print('Plot: ',films['plot'])
            print('Rating: ',films['rating'],'\n')
    except:
        pass

    


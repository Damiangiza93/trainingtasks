'''
Napisz program liczący odległość liniową między dwoma dowolnymi punktami na mapie, wykorzystujący ich współrzędne geograficzne (długość i szerokość 
geograficzną). Wykorzystaj dowolny algorytm, np. https://pl.wikibooks.org/.../Astrono.../Odleg%C5%82o%C5%9Bci
Skorzystaj z API (np. https://rapidapi.com/trueway/api/trueway-geocoding), żeby obliczyć odległość pomiędzy twoim adresem, a charakterystycznymi 
punktami np. Wieżą Eiffla czy Tadź Mahal.

Propozycja rozszerzenia: zamiast podawać swój adres, użyj geolokalizacji
'''

import requests
from math import sqrt, cos, pi
import geocoder

api_key = "fe6b113cacmsh408e7551c973e91p1ec335jsna41eb97e6e86"

def localization(address):
    url = "https://trueway-geocoding.p.rapidapi.com/Geocode"
    querystring = {"address":address,"language":"pl"}
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "trueway-geocoding.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()['results'][0]

g = geocoder.ip('me')
myloc = g.address
goloc = input('Lokalizacja docelowa (ul lub miejsce, miasto, państwo):')

my_loc = localization(myloc)
go_loc = localization(goloc)

d_len = sqrt(
            ((go_loc['location']['lat'] - my_loc['location']['lat'])**2) +
            (cos(my_loc['location']['lat'] * pi / 180) * (go_loc['location']['lng'] - my_loc['location']['lng']))**2) * (40075.704/360)

print(f'{goloc} jest {d_len:.2f}km od {myloc}')


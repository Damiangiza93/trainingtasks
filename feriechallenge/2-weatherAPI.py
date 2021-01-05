'''
Napisz program, który po uruchomieniu wyświetla w czytelnej formie aktualną datę, godzinę, dzień tygodnia i pogodę/temperaturę/ciśnienie 
w zadanym mieście (wykorzystaj np. https://rapidapi.com/commu.../api/open-weather-map/endpoints - pamiętaj o poprawnym przeliczeniu jednostek 
np. temperatura z kelwinów na stopnie) oraz losowy cytat (np. https://type.fit/api/quotes ). Wykorzystaj requests i datetime.
Propozycja rozszerzenia: Wyświetl również bieżący czas dla miast w różnych strefach czasowych (np. Pekin, Sydney, Waszyngton, Londyn) - 
wykorzystaj np. pytz: https://pypi.org/project/pytz/ oraz wyświetl listę osób obchodzących imieniny 
(poszukaj otwartej bazy danych lub wykorzystaj prosty web scrapping np. z wykorzystaniem: https://imienniczek.pl/widget/js ).
'''

from datetime import datetime
import calendar
import requests
import pytz
import random

url = "https://community-open-weather-map.p.rapidapi.com/weather"

city = input('Write the city: ')
querystring = {"q":city,"lat":"0","lon":"0","id":"2172797","lang":"eng","units":"metric"}
headers = {
    'x-rapidapi-key': "fe6b113cacmsh408e7551c973e91p1ec335jsna41eb97e6e86",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
d = response.json()

''' data godzina dzien tygodnia '''
timezone = (d['timezone'] // 3600)
if timezone >= 0:
    timezone = f'Etc/GMT-{timezone}'
else:
    timezone = f'Etc/GMT+{-timezone}'

my_date = datetime.now(pytz.timezone(timezone)).isoformat(sep=' ', timespec='seconds')
print('date and time:',my_date)
weekday = datetime.now(pytz.timezone(timezone)).weekday()
print('weekday:',calendar.day_name[weekday], '\n')

''' pogoda temperatura ciśnienie '''

print('weather:', d['weather'][0]['description'])
print('temperature:', d['main']['temp'], ' deegree Centigrade')
print('pressure:', d['main']['pressure'], ' hPa \n')

''' losowy cytat '''

url1 = "https://type.fit/api/quotes"
response = requests.request("GET", url1)
q = response.json()
quote = random.choice(q)
print('Quote of the day:\n',f'"{quote["text"]}"')
print('Author:',quote['author'])


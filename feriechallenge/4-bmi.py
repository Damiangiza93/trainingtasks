'''
Napisz program, który na podstawie masy [kg] i wzrostu [cm] wylicza wskaźnik BMI (https://en.wikipedia.org/wiki/Body_mass_index) oraz 
informuje użytkownika, w jakim jest zakresie. Zakresy można wpisać “z palca” (ale może nieco mądrzej niż ciągiem if-elif-else dla każdego zakresu! 😉 ) 
albo odczytać z dowolnego API, np. https://rapidapi.com/navii/api/bmi-calculator . 

Następnie program losuje jedną z aktywności fizycznych oraz czas 
jej wykonania, np. bieganie przez 30 minut. Czas nie może być dłuższy niż podany przez użytkownika (maksymalny czas, który można poświęcić na ćwiczenia). 
Zadbaj o to, aby czas aktywności był jakoś uzależniony od BMI (na przykład osoba z niedowagą nie powinna ćwiczyć mniej niż osoba o wadze normalnej - 
ustal pewien minimalny czas; ale już osoba z nadwagą powinna ćwiczyć dłużej - ustal odpowiedni nieliniowy mnożnik, tak aby nie przekroczyć maksimum). 
Utwórz w ten sposób plan treningowy na 7 następnych dni, wyniki zapisując do pliku .txt.

Propozycja rozszerzenia: przygotuj urozmaicony plan treningowy uwzględniający maksymalny czas wpisany przez użytkownika - kilka aktywności fizycznych 
ma wypełniać całą dzienną ilość czasu, mają zajmować jakąs ustaloną minimalną długość (np. 10 minut) oraz nie mogą się powtarzać jednego dnia.
'''
import random
import calendar

''' bmi '''

height = float(input('height in meters (np. 1.85):'))
mass = float(input('mass in kg:'))

bmi = mass / (height**2) 
print('your BMI:', format(bmi, '.2f'))
categories = [
            [0,15,'very severely underweight'],
            [15,16,'severely underweight'],
            [16,18.5,'underweight'],
            [18.5,25,'normal'],
            [25,30,'overweight'],
            [30,35,'obese class 1'],
            [35,40,'obese class 2'],
            [40,60,'obese class 3']]

for i in categories:
    if i[0]<bmi<=i[1]:
        print('Your weight is:',i[2])

''' ćwiczenia '''
maxtime = float(input('maximum training time in minutes:'))
ex_list = ['running', 'bike', 'swimming', 'crossfit', 'skating']

if bmi <= 16:
    mult = 0.5
elif bmi<=25:
    mult = 0.75
elif bmi<=35:
    mult = 0.9
else:
    mult = 1

time = mult * maxtime

with open('training.txt', 'w') as f:
    f.write('Training plan \n')
        
    for i in range(7):
        excercise = random.choice(ex_list)
        f.write(f'{calendar.day_name[i]} - {excercise} - {time} minutes\n')

    


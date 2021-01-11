'''
Napisz program, który w wybranej lokalizacji odczyta wszystkie pliki graficzne (w określonych formatach, np. jpg, png, bmp itp.), następnie zmniejszy 
ich rozdzielczość o 50% i zapisze je w podkatalogu “smaller” z odpowiednimi nazwami. Wykorzystaj pillow lub inną bibliotekę do pracy z obrazami. 
Propozycja rozszerzenia: Oblicz ile miejsca na dysku można oszczędzić po kompresji (odczytaj rozmiar plików w pierwotnym folderze oraz "smaller" 
i porównaj obie wartości - bezwzględnie i w %)
'''

from PIL import Image
import os

#paths - folder ze zdjeciami | extension - jakie rozszerzenie ma brać pod uwagę | nazwa folderu w którym zapisze nowe zdjęcia
paths = 'D:/Zdjecia/ja/'
os.chdir(paths)
extension = '.JPG'
sfolder = 'smaller'

for f in os.listdir('.'):
    if f.endswith(extension):
        im = Image.open(f)                              
        name, fext = os.path.splitext(f)                
        size = []
        for s in im.size:                               
            size.append(int(s//2))            
        im.thumbnail(size)                              
        if size[1] < size[0]:                           
            im.transpose(Image.ROTATE_90).save(f'{paths}{sfolder}/{name}half{fext}')
        else:
            im.save(f'{paths}{sfolder}/{name}half{fext}')

s1 = 0
for f in os.listdir(paths):
    if f.endswith(extension):
        s1 += os.path.getsize(f'{paths}{f}')
s2 = 0
for f in os.listdir(f'{paths}{sfolder}'):
    if f.endswith(extension):
        s2 += os.path.getsize(f'{paths}{sfolder}/{f}')

print(f'before: {s1/1048576:.2f} Mb\nafter:  {s2/1048576:.2f} Mb')





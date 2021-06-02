#первый вариант
from collections import *
slovar = defaultdict(list)
dicts = {'name': 'ivan', 'surname': 'ivanov'}
for key, value in dicts.items():
    slovar[value].append(key)
print(slovar)





#Второй вариант
slovar = {'name': 'ivan', 'surname': 'ivanov'}
new_slovar ={}
for key, value in slovar.items():
    new_slovar[value] = key
print(new_slovar)

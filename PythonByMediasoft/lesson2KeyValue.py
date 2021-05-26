from collections import *
slovar = defaultdict(list)
dicts = {'name': 'ivan', 'surname': 'ivanov'}
for key, value in dicts.items():
    slovar[value].append(key)
print(slovar)
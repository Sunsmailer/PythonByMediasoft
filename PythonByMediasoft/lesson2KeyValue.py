slovar = {'name': 'ivan', 'surname': 'ivanov'}
new_slovar ={}
for key, value in slovar.items():
    new_slovar[value] = key
print(new_slovar)

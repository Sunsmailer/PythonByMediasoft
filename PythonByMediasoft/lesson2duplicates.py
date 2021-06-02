#первый вариант
duplicates = ['1', '2', '3', '3', '6', '4', '5', '6']
new_duplicates = []
[new_duplicates.append(item) for item in duplicates if item not in new_duplicates]
new_duplicates.sort()
print(new_duplicates)



#второй вариант
dup1 = {'1', '2', '3', '3', '6', '4', '5', '6'}
dup2 = {'1', '2', '3', '4', '5','6'}
dup = dup1.union(dup2) #через пересечение
dup = sorted(dup)
print(dup)

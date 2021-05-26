duplicates = ['1', '2', '3', '3', '6', '4', '5', '6']
new_duplicates = []
[new_duplicates.append(item) for item in duplicates if item not in new_duplicates]
new_duplicates.sort()
print(new_duplicates)
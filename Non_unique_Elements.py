data = ([10, 9, 10, 10, 9, 8])
temp_data = data.copy()
data_non_unique = []
while data != []:
    if temp_data.count(data[0]) > 1:
        data_non_unique.append(data[0])
        data.remove(data[0])
    else:
        data.remove(data[0])
print(data_non_unique)

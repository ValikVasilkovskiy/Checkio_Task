#Входные данные: Массив как список (list) чисел (int).
#Выходные данные: Медиана как число (int, float).
#Пример median([1, 2, 3, 4, 5]) == 3
#assert median([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"

def median(data):
    data.sort()
    return (lambda data: ((data[int(len(data) / 2)] + data[int(len(data) / 2 - 1)])) / 2 if len(data) % 2 == 0 else data[
        len(data) // 2])(data)
#    if len(data) % 2 == 0:
#        median_data = ((data[int(len(data)/2)] + data[int(len(data)/2 - 1)])) / 2
#    else:
#        median_data = data[len(data) // 2]
#    return median_data
print(median([3]))

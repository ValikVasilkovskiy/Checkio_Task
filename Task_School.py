time_start = 9
number = int(input())
time_end = 0
for i in range(1, number + 1):
    if i != number:
        if i % 2 == 0:
            time_end += (45 + 15)
        else:
            time_end += (45 + 5)
    else:
        time_end += 45
print((time_start + (time_end // 60)), (time_end % 60))
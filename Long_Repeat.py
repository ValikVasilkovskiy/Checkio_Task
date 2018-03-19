line = ('aafkgfkjghhghhghghfgkkkkk')
maximum = 1
long = 1
temp = 0
if len(line) >= 2:
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            long += 1
        else:
            if long > maximum:
                maximum = long
                long = 1
            else:
                long = 1
elif line == '':
    print(0)
if long >= maximum:
    print(long)
else:
    print(maximum)

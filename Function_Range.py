def modify_range(*args):
    if len(args) > 3 or len(args) == 0:
        raise('format function ([start,] end [,step])')
    if len(args) == 1:
        start = 0
        end = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        end = args[1]
        step = 1
    else:
        start = args[0]
        end = args[1]
        step = args[2]
    if start < end and step > 0:
        while start < end:
            yield start
            start += step
    elif start > end and step < 0:
        while start > end:
            yield start
            start += step


# test
for i in modify_range(-1, -10, -1):
    print(i, end=' ')
print()
for i in range(-1, -10, -1):
    print(i, end=' ')
print()
for i in modify_range(10):
    print(i, end=' ')
print()
for i in range(10):
    print(i, end=' ')
print()
for i in modify_range(4, 10):
    print(i, end=' ')
print()

# test
for i in range(4, 10):
    print(i, end=' ')
print()
for i in modify_range(10, 1, -1):
    print(i, end=' ')
print()
for i in range(10, 1, -1):
    print(i, end=' ')
print()
for i in modify_range(-10, -1, 1):
    print(i, end=' ')
print()
for i in range(-10, -1, 1):
    print(i, end=' ')
print()

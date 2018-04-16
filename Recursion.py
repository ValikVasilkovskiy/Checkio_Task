def deep(data):
    stack = []
    list(map(lambda x: stack.append(x) if '__iter__' not in dir(x) else stack.extend(deep(x)), data))
    return stack

def search_deep(data):
    stack = []
    for i in data:
        if '__iter__' not in dir(i):
            stack.append(i)
        else:
            stack.extend(search_deep(i))
    return stack

assert deep([1, [1, 2], [[[1]]], -2]) == [1, 1, 2, 1, -2]
assert deep([[1], [[-1], 2], [[[1]]], -2]) == [1, -1, 2, 1, -2]
assert deep([1, 2, 3, 4]) == [1, 2, 3, 4]
assert deep([1,]) == [1]


assert search_deep([1, [1, 2], [[[1]]], -2]) == [1, 1, 2, 1, -2]
assert search_deep([[1], [[-1], 2], [[[1]]], -2]) == [1, -1, 2, 1, -2]
assert search_deep([1, 2, 3, 4]) == [1, 2, 3, 4]
assert search_deep([1,]) == [1]






















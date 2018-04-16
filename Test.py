def deep(data):
    list(map(lambda x: deep(x) if '__iter__' in dir(x) else print(x, end=' '), data))


def search_deep(data):
    stack = []
    for i in data:
        if '__iter__' not in dir(i):
            stack.append(i)
        else:
            stack.extend(search_deep(i))
    return stack




















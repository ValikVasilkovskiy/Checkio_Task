def split_pattern(data):
    stack = []
    for i in data:
        if i == '?':
            stack.append(i)
            data = data[data.index(i)+1:]
        elif i == '[':
            stack.append(data[data.index(i): data.index(']')+1])
            data = data[data.index(']')+1:]
        else:
            stack.append(i)
    return stack
def unix_match(filename: str, pattern: str):
    list_filename = []
    for i in filename: list_filename.append(i)
    list_pattern = split_pattern(pattern)
    #for i in range(len(list_filename)):
        #if list_pattern[i] == '*':
            #list_pattern.insert(i, '*')
    print(list_pattern)
    print(list_filename)

print(unix_match('filename.txt', 'fi*me.txt'))


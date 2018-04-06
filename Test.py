import itertools

def domino_chain(tiles: str):
    list_stack = []
    temp_stack = []
    for i in tiles:
        if i.isdigit():
            temp_stack.append(int(i))
            if len(temp_stack) == 2:
                list_stack.append(temp_stack)
                #if list(reversed(temp_stack)) not in list_stack:
                #    list_stack.append(list(reversed(temp_stack)))
                temp_stack = []

    combination_stack = []
    for i in list_stack:
        for j in list_stack:
            if i != j:
                if i[1] == j[0]:
                    temp_stack.append(i)
                    temp_stack.append(j)
                    if temp_stack not in combination_stack:
                        combination_stack.append(temp_stack)
                    temp_stack = []
                if list(reversed(i))[1] == j[0]:
                    temp_stack.append(list(reversed(i)))
                    temp_stack.append(j)
                    if temp_stack not in combination_stack:
                        combination_stack.append(temp_stack)
                    temp_stack = []
                if i[1] == list(reversed(j))[0]:
                    temp_stack.append(i)
                    temp_stack.append(list(reversed(j)))
                    if temp_stack not in combination_stack:
                        combination_stack.append(temp_stack)
                    temp_stack = []
                if list(reversed(i))[1] == list(reversed(j))[0]:
                    temp_stack.append(list(reversed(i)))
                    temp_stack.append(list(reversed(j)))
                    if temp_stack not in combination_stack:
                        combination_stack.append(temp_stack)
                    temp_stack = []

    for i in combination_stack:
        print(i)

print(domino_chain("0-2, 0-5, 1-5, 1-3, 5-5"))
















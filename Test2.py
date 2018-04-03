import itertools

def domino_chain(tiles: str):
    list_stack = []
    temp_stack = []
    for i in tiles:
        if i.isdigit():
            temp_stack.append(int(i))
            if len(temp_stack) == 2:
                list_stack.append(temp_stack)
                if list(reversed(temp_stack)) not in list_stack:
                    list_stack.append(list(reversed(temp_stack)))
                temp_stack = []
    tuple_stack = tuple(map(lambda x: tuple(x), list_stack))
    comb1 = []
    combinations = set(itertools.permutations(tuple_stack, 2))
    for i in combinations:
        for j in range(len(i)-1):
            if i[j][1] == i[j+1][0]:
                if set(i[j]) != set(i[j+1]):
                    comb1.append(i)
    set(comb1)
    for i in tuple(itertools.permutations(comb1, 2)):
        print(i)



print(domino_chain("0-2, 0-5, 1-5, 1-3, 5-5"))


import itertools

def domino_chain(tiles: str):
    stack, temp_stack = [], ''
    for i in tiles:
        if i.isdigit():
            temp_stack += i
            if len(temp_stack) == 2:
                stack.append(temp_stack)
                temp_stack = ''
    combinations = []

    for i in tuple(itertools.permutations(stack, len(stack))):
        for j in range(len(i)-1):
            if i[j][0] not in i[j+1] and i[j][1] not in i[j+1]:
                break
        else:
            if i not in combinations and tuple(reversed(i)) not in combinations:
                combinations.append(i)
    return len(combinations)


print(domino_chain("0-2, 0-5, 1-5, 1-3, 5-5")) # return 1 combination
print(domino_chain("1-5, 2-5, 3-5, 4-5, 3-4")) # return 2 combination
print(domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4")) # return 0 combination
print(domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4")) # 6


import itertools

def domino_chain(tiles: str):
    stack, temp_stack, chain_stack, r, next_stack = [], [], [], len(tiles.split(',')), []
    for i in tiles:
        if i.isdigit():
            temp_stack.append(int(i))
            if len(temp_stack) == 2:
                stack.append(temp_stack)
                next_stack.append(temp_stack)
                stack.append(list(reversed(temp_stack)))
                temp_stack = []
    for i in list(itertools.permutations(stack, r)):
        for j in range(len(i)-1):
            if i[j][1] != i[j+1][0]:
                break
        else:
            for part in next_stack:
                if part in i or list(reversed(part)) in i:
                    continue
                else:
                    break
            else:
                if i not in chain_stack and tuple(reversed(tuple(map(lambda x: list(reversed(x)),i)))) not in chain_stack:
                    chain_stack.append(i)
    return len(chain_stack)

# test
#print(domino_chain("0-2, 0-5, 1-5, 1-3, 5-5")) # return 1 combination
#print(domino_chain("1-5, 2-5, 3-5, 4-5, 3-4")) # return 2 combination
#print(domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4")) # return 0 combination
print(domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6")) # 28



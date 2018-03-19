def second_index(text: str, symbol: str):
    fist_index = 0
    if text != '':
        for i in range(len(text)):
            if text[i] == symbol:
                fist_index +=1
                if fist_index == 2:
                    return (i)
second_index("hi mr Mayor", " ")
def striped_words(text):
    dict = {'A': 'BCDFGHJKLMNPQRSTVWXZ', 'E': 'BCDFGHJKLMNPQRSTVWXZ', 'I': 'BCDFGHJKLMNPQRSTVWXZ',
            'O': 'BCDFGHJKLMNPQRSTVWXZ', 'U': 'BCDFGHJKLMNPQRSTVWXZ', 'Y': 'BCDFGHJKLMNPQRSTVWXZ'}
    temp_stack2, temp_stack, stack, temp = [], [], [], ''
    #заполняем стек только словами, которые состоят из букв и цыфр
    for i in text:
        if str(i).isalnum():
            temp += i.upper()
        else:
            if temp != '':
                stack.append(temp)
                temp = ''
    if temp != '':
        stack.append(temp)
    #заполняем стек значениями длиной меньше двух (неудолетворяющими полосатость)
    list(map(lambda x: temp_stack2.append(x) if len(x) < 2 else x, stack))
    #удаляем из основного стека значения которые меньше двух (неудолетворяющие)
    for i in temp_stack2:
        if i in stack:
            stack.remove(i)
    #проверяем на полосатость все слова
    for i in range(len(stack)):
        compare = []
        for j in stack[i]:
            if compare == []:
                compare.append(j)
            else:
                if j in dict:
                    if compare[-1] in dict[j]:
                        compare = j
                    else:
                        temp_stack.append(stack[i])
                        compare = []
                elif j not in dict:
                    if compare[-1] in dict:
                        compare = j
                    else:
                        temp_stack.append(stack[i])
                        compare = []
                else: #если в слове число, слово заносится в стек неудолетворяющих слов
                    temp_stack.append(stack[i])
                    compare = []
    #проверяем, если в стеке не удолетворяющие слова
    for i in temp_stack:
        if i in stack:
            stack.remove(i)
    return len(stack)
print(striped_words("1 2 3 12 13"))
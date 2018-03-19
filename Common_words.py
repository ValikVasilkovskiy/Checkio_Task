def common(first, second):
    stack1, stack2, temp_stack, sort_stack, line_stack = [], [], '', [], ''
    #наполняем первый стек элементами первой строки
    for i in first:
        if str(i).isalpha():
            temp_stack += i
        else:
            stack1.append(temp_stack)
            temp_stack = ''
    if temp_stack != '':
        stack1.append(temp_stack)
        temp_stack = ''
    #наполняем второй стек элементами второй строки
    for i in second:
       if str(i).isalpha():
           temp_stack += i
       else:
           stack2.append(temp_stack)
           temp_stack = ''
    if temp_stack != '':
        stack2.append(temp_stack)
    #находим одинаковые элементы в двух стеках
    for i in stack1:
        if i in stack2:
            sort_stack.append(i)
    #наполняем и сортируем результирующий стек
    sort_stack.sort()
    #преобразовываем список в строку
    line_stack = ','.join(sort_stack)
    return line_stack

print(common("one,two,three", "four,five,one,two,six,three"))
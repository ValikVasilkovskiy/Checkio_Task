def brackets(expression):
    stack = ['']
    data = ('(', '[', '{', ')', ']', '}')
    dict = {'}': '{', ')': '(', ']':'['}
    for i in expression:
        if i in data:
            if i not in dict:
                stack.append(i)
            else:
                if dict[i] != stack[-1] or stack == ['']:
                    return False
                else:
                    stack.pop()
    if stack == ['']:
        return True
    else:
        return False


print(brackets("(({[(((1)-2)+3)-3]/3}-3)"))

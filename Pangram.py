def check_pangram(text):
    stack = []
    if len(text) < 26:
        return False
    else:
        for i in text.lower():
            if i.isalpha():
                if i not in stack:
                    stack.append(i)
                    if len(stack) == 26:
                        return True
    return False

print(check_pangram("Six big devils from Japan quickly forgot how to walt."))

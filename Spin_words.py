def spin_words(sentence):
    stack = ''
    for i in sentence.split(' '):
        if len(i) >= 5:
            stack += i[::-1] + ' '
        else:
            stack += i + ' '
    return stack.rstrip()

# test
print(spin_words("Hey fellow warriors"))

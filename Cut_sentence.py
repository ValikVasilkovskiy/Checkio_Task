"""
Input: Two arguments:
one-line sentence as a string
max length of the truncated sentence as an int
Output: The shortened sentence plus the ellipsis (if required) as a one-line string.
Examples:
cut_sentence("Hi my name is Alex", 4) == "Hi..."
cut_sentence("Hi my name is Alex", 8) == "Hi my..."
cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"
cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex
"""
def cut_sentence(line, length):
    stack = line.split(' ')
    str_stack = ''
    if line[:length] != line:
        for i in line[:length].split(' '):
            if i in stack:
                str_stack += (i + ' ')
        return str_stack.rstrip() + '...'
    else:
        return line

# test
print(cut_sentence("Hi my name is Alex", 4))
print(cut_sentence("Hi my name is Alex", 9))
print(cut_sentence("Hi my name is Alex", 18))
print(cut_sentence("Hi my name is Alex", 10))
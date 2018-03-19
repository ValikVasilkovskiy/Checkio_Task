"""
Input: A sequence of commands as a list of strings.
Output: The queue remaining as a string.
Example: letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT"
"""
def letter_queue(commands):
    stack, string_stack = [], ''
    for i in commands:
        if i.startswith('PUSH'):
            stack.append(i[-1])
        elif i.startswith('POP'):
            if stack != []:
                stack.pop(0)
    # list convert to string
    for i in stack: string_stack += i
    return string_stack

# test
print(letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]))
# Input: Words as a set of strings.
# Output: True or False, as a boolean.
# Example: words_set({"hello", "lo", "he"}) == True
# Example: words_set({"hello", "la", "hellow", "cow"}) == False

def end_with(words_set):
    temp_stack = list(words_set)
    for i in words_set:
        # del i-element
        temp_stack.remove(i)
        # list without i-element
        for j in temp_stack:
            if j.endswith(i):
                return True
        # add i-element in list
        temp_stack.append(i)
    return False

"""
Input data: A nested list with integers.
Output data: The one-dimensional list with integers.
Example:
flat_list([1, 2, 3]) == [1, 2, 3]
flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
"""
def flat_list(array):
    r, s, t = [], str(array), ''
    for i in range(len(s)):
        if s[i].isdigit() or s[i] == '-':
            t += s[i]
        else:
            if t:
                r.append(int(t))
                t = ''
    return r

# test
print(flat_list([[[2]], [4, [5, 6, [-69], 6, 6, 6], 7]]))

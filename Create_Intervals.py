# Input: A set of ints.
# Output: A list of tuples of two ints, indicating the endpoints of the interval.
# The Array should be sorted by start point of each interval
# Examples: create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
# Examples: create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]

def create_intervals(data):
    stack, temp_stack, main_stack, buffer_stack = [], [], [], []
    stack = sorted(data)
    for i in stack:
        if not temp_stack:
            temp_stack.append(i)
            buffer_stack.append(i)
        else:
            # the step is 1 ?
            if i - buffer_stack[-1] != 1:
                temp_stack.append(buffer_stack[-1])
                main_stack.append(temp_stack)
                temp_stack = []
                buffer_stack = []
                temp_stack.append(i)
                buffer_stack.append(i)
            else:
                buffer_stack.append(i)
    # generate view for len(temp_stack) = 1 as (12, 12)
    if temp_stack:
        temp_stack.append(buffer_stack[-1])
        main_stack.append(temp_stack)
    # out on view [(), (), ()]
    return list(map(lambda i: tuple(i), main_stack))
# test 1
print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}))
# test 2
print(create_intervals({1, 2, 3, 6, 7, 8, 4, 5}))

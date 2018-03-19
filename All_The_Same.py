def all_the_same(elements:list):
    if elements:
        if elements.count(elements[0]) != len(elements):
            return False
    return True

# test
print(all_the_same(['a', 'b', 'a']))
print(all_the_same(['a', 'a', 'a']))
print(all_the_same(['a', 'b', 'c']))
print(all_the_same([1, 1, 1]))
print(all_the_same([1, 2, 1]))


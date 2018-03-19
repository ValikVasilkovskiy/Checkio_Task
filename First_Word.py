def first_word(text: str):
    slice_start = 0
    slice_end = len(text)
    for i in range(len(text)):
        if text[i].isalpha():
            slice_start = i
            break
    for j in range(slice_start, len(text)):
        if text[j].isalpha() or text[j] == "'":
            continue
        else:
            slice_end = j
            break
    return (text[slice_start:slice_end])
first_word("greetings, friends")


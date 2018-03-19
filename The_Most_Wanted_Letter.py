def checkio(text):
    count_letter = 1
    most_wonted = []
    for i in range(len(text)):
        if text.lower()[i].isalpha():
            if text.lower().count(text.lower()[i]) > count_letter:
                count_letter = text.lower().count(text.lower()[i])
                most_wonted.clear()
                most_wonted.append(text.lower()[i])
            elif text.lower().count(text.lower()[i]) < count_letter:
                continue
            elif text.lower().count(text.lower()[i]) == count_letter:
                most_wonted.append(text.lower()[i])
        else:
            continue
    most_wonted.sort()
    result = most_wonted[0]
    return print(result)


def correct_sentence(text: str):
    if text != '':
        if text.istitle():
            text = text
        else:
            text = text[0].upper() + text[1:]
        if text.endswith('.'):
            text = text
        else:
            text += '.'
    return print(text)

correct_sentence('')
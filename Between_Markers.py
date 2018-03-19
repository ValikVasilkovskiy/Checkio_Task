def between_markers(text: str, begin: str, end: str):
    if text.find(begin) == -1 and text.find(end) >= 0:
        return text[:text.find(end)]
    elif text.find(end) == -1 and text.find(begin) >= 0:
        return text[text.find(begin) + len(begin):]
    elif text.find(begin) >= 0 and text.find(end) >= 0:
        return text[text.find(begin) + len(begin): text.find(end)]
    elif text.find(begin) == -1 and text.find(end) == -1:
        return text
    elif text.find(end) > text.find(begin):
        return ''
print(between_markers('No[/b] hi', '[b]', '[/b]'))



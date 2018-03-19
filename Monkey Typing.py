text = ("How aresjfhdskfhskd you?")
words = {"how", "are", "you", "hello"}
item_in_text = 0
text_temp = text.lower()
for i in words:
    if i in text_temp:
        item_in_text += 1
        continue
    else:
        continue
print(item_in_text)

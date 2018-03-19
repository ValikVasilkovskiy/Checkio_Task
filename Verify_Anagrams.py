def verify_anagrams(first_word, second_word):
   stack1, stack2, anagrams = '', [], True
   for i in first_word:
       if str(i).isalpha():
           stack1 += str(i).lower()
   list(map(lambda i: stack2.append(str(i).lower()) if str(i).isalpha() else i, second_word))
   for i in stack1:
       if i in stack2:
           stack2.remove(i)
       else:
           return False
   if stack2 != []:
       return False
   return anagrams
print(verify_anagrams("Kyoto", "Tokyo"))


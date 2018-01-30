def dict_making():
   dictionary=dict()
   with open('sorted_words.txt','r') as readMode:
      for word in readMode:
         word=word.strip().lower()
         letter=word[0]
         if letter not in dictionary:
            dictionary[letter]=[]
         dictionary[letter].append(word)
         #print(dictionary)
         #break
   print(dictionary)
dict_making()

from pprint import pprint 
#document= open('LIWC_words.txt')
#liwcwords = document.readline()
#print(type(iwcwords))
with open('LIWC_words.txt','r') as liwcwords:
   #print(liwcwords)
   di =dict()
   for line in liwcwords:
      #print(line)
      #break
      line_list=line.split()
      if line_list:
         di.update({line_list[0]:line_list[1:]})
pprint(di)

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
Palabras = list()
for line in fh:
 line.rstrip()
 Palabras=line.split()

 for word in Palabras:
   if word not in lst:
       lst.append(word)



lst.sort()
print(lst)

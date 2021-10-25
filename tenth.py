name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts=dict()
email=list()

for line in handle:
    line.rstrip()
    if not line.startswith('From '):continue
    words=line.split()
    email.append(words[1])


for word in email:
        counts[word]=counts.get(word,0)+1
#print (counts)#
Bigcount=None
Bigword=None
for word,count in counts.items():
  if Bigcount is None or count > Bigcount:
      Bigword = word
      Bigcount = count

print (Bigword,Bigcount)

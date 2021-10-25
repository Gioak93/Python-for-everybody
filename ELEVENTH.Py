name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
archivo = open(name)

counts=dict()
email=list()

for line in archivo:

    line.rstrip()
    if not line.startswith('From '):continue
    words=line.split()
    email.append(words[5])

hours = []

for hour in email:
    hours.append( hour.split(':')[0] )
print(hours)
for keys in hours:  #creamos las llaves o keys

    counts[keys]=counts.get(keys,0)+1  #vamos contando las veces que se repite o creamos una nueva

print(counts)
for keys, count in sorted(counts.items()):  #organizamos en orden numerico del menor al mayor los keys

    print (keys, count)
print(type(hours))

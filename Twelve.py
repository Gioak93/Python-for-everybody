import re
name = input("Enter File",)
handle = open(name)
numbers = list()
numero = None
for line in handle:
    line.rstrip()                                #quitamos los espacios
    x = re.findall( '[0-9]+' , line)             #encontramos los valores numericos
    if len(x) == 0: continue                      #si la linea no tiene ningun numero pasamos
    n = int(len(x))                                     #definimos el subindice para transforamr cada numero en un float
    for num in x:               #definimos la condicion
        num = float(x[n-1])                        #convertimos cada numero en float
        n=n-1                                       #disminuimos valor de indice
        numbers.append(num)                         #anadimos el valor a la lista

sumatoria = sum(numbers)                            #sumamos todo
print (sumatoria)

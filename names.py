name = input ('Ingrese su nombre:  ',)

print( 'Hola', name)

edad = input ('Cual es tu edad:' ,)
age=float(edad)
if age <= 18:
    print ('Entonces eres joven')
elif age < 35:
    print ('Entonces eres un adulto joven')
elif age < 60:
    print ('Entonces eres adulto')
else:

    print ('Entonces ya estas en la tercera edad')

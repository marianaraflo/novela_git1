#Primer ejercicio#
edad1= int(input("Ingresa la edad de Carmen: "))
edad2= int(input("Ingrese la edad de Laika: "))
if (edad1 > edad2):
    print("Carmen es más grande")
else:
   print("Laika es más grande")

#Segundo ejercicio#
cadena= str(input("ingrese la cadena: "))
if cadena == ''.join(reversed(cadena)):
    print(cadena, "es palíndromo")
else:
    print(cadena, "no es palíndromo")
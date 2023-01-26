import math

o = 3
p = 4
print(o+p)
print(o-p)
print(o*p)
print(o**p)
print(o/p)

x = int(input("Hola dime un número"))
z = int(input("Vale, ahora dime otro número"))
print("Ahora haré los siguientes calculos")
print("suma")
print(x+z)
print("resta")
print(x-z)
print("multiplicación")
print(x*z)
print("potencia")
print(x**z)
print("división")
print(x/z)

a = int(input("Hola, a continuación haremos una ecuación de segundo grado.Dame un número para que sea a."))
b = int(input("Ahora dime oro número para que sea b."))
c = int(input("Finalmente dime otro número para que sea c."))

disc=(b**(2)-4*a*c)

if disc<0:
    print("No tiene solución, prueba con  otros números")
if disc==0:
    print((-b+math.sqrt(disc))/(2*a))
if disc>0: 
     print((-b+math.sqrt(disc))/(2*a))
     print((-b-math.sqrt(disc))/(2*a))
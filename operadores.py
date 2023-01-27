a = int(input("Buenas, dime oro número para que sea a."))
b = int(input("Ahora dime oro número para que sea b."))

if a==b:
    print("Son iguales.")
elif a != b:
    print("No son iguales.")
if a > b:
    print("El primer número es superior al segundo.")
elif a < b:
    print("El segundo número es superior al primero.")

a > b # False
a >= b # False
a < b # True

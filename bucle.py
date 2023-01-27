# while
numero1 = 4

numero2 = int(input("Dime un número por favor. "))


while  numero1 != numero2:
    if numero1 < numero2:
        print("El número mágico es más pequeño.")
    else:
        print("El número mágico es más grande.")
    numero2 = int(input("Dime un número por favor. "))

print("Enhorabuena!")
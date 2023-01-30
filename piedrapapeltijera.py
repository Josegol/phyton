import random
user = input("Buenas usuario, ahora jugaremos al Piedra, Papel, Tijera, elige una de estas opciones.")
pc = random.randint(1,3)
if user == "Piedra":
    user =1
if user == "Papel":
    user =2
if user == "Tijera":
    user =3

if user == pc:
    print("Empate")

if user == 1 and pc == 2:
    print("Has perdido...")
if user == 1 and pc == 3:
    print("Has ganado!!!")

if user == 2 and pc == 1:
    print("Has ganado!!!")
if user == 2 and pc == 3:
    print("Has perdido...")

if user == 3 and pc == 1:
    print("Has perdido...")
if user == 3 and pc == 2:
    print("Has ganado!!!")
if pc == 1:
    pc = "piedra"
if pc == 2:
    pc = "tapel"
if pc == 3:
    pc = "tijera"
print("He sacado "+pc)


    
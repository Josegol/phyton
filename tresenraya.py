
import random
casillas = ["","","","","","","","",""]
casillas_libres = [0,1,2,3,4,5,6,7,8]

player = input("¿Hola jugador, quieres ser x/o? ")
if player == "x":
    pc = "o"
if player == "o":
    pc = "x"

final = False

while not final:

    posicion = int(input("Ahora jugaremos al tres en raya, elige una casilla del 0 al 8. "))
    casillas[posicion]= player
    casillas_libres.remove(posicion)
    
    posicion = random.choice(casillas_libres)
    casillas[posicion] = pc
    casillas_libres.remove(posicion)

    print(" |  "+casillas[0]+" |  "+casillas[1]+" |  "+casillas[2]+"  | ")
    print(" |  "+casillas[3]+" |  "+casillas[4]+" |  "+casillas[5]+"  | ")
    print(" |  "+casillas[6]+" |  "+casillas[7]+" |  "+casillas[8]+"  | ")

    if casillas[0] == casillas[1] == casillas[2] == player:
        print("Has ganado!!!") 
        final = True
    if casillas[3] == casillas[4] == casillas[5] == player:
        print("Has ganado!!!")
        final = True
    if casillas[6] == casillas[7] == casillas[8] == player:
        print("Has ganado!!!")
        final = True
    if casillas[0] == casillas[3] == casillas[6] == player:
        print("Has ganado!!!")
        final = True
    if casillas[1] == casillas[4] == casillas[7] == player:
        print("Has ganado!!!")
        final = True
    if casillas[2] == casillas[5] == casillas[8] == player:
        print("Has ganado!!!")
        final = True
    if casillas[0] == casillas[4] == casillas[8] == player:
        print("Has ganado!!!")
        final = True
    if casillas[2] == casillas[4] == casillas[6] == player:
        print("Has ganado!!!")
        final = True

    if casillas[0] == casillas[1] == casillas[2] == pc:
        print("Has perdido...")
        final = True
    if casillas[3] == casillas[4] == casillas[5] == pc:
        print("Has perdido...")
        final = True
    if casillas[6] == casillas[7] == casillas[8] == pc:
        print("Has perdido...")
        final = True
    if casillas[0] == casillas[3] == casillas[6] == pc:
        print("Has perdido...")
        final = True
    if casillas[1] == casillas[4] == casillas[7] == pc:
        print("Has perdido...")
        final = True
    if casillas[2] == casillas[5] == casillas[8] == pc:
        print("Has perdido...")
        final = True
    if casillas[0] == casillas[4] == casillas[8] == pc:
        print("Has perdido...")
        final = True
    if casillas[2] == casillas[4] == casillas[6] == pc:
        print("Has perdido...")
        final = True

if casillas_libres == []:
    print(Empate)
    final = True
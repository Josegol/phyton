
import random
casillas = ["","","","","","","","",""]

posicion = int(input("Ahora jugaremos al tres en raya, elige una casilla del 0 al 8"))
player = "x"
casillas[posicion]= player

if casillas[0] == casillas[1] == casillas[2] == player:
    print("Has ganado!!!")
if casillas[3] == casillas[4] == casillas[5] == player:
    print("Has ganado!!!")
if casillas[6] == casillas[7] == casillas[8] == player:
    print("Has ganado!!!")
if casillas[0] == casillas[3] == casillas[6] == player:
    print("Has ganado!!!")
if casillas[1] == casillas[4] == casillas[7] == player:
    print("Has ganado!!!")
if casillas[2] == casillas[5] == casillas[8] == player:
    print("Has ganado!!!")
if casillas[0] == casillas[4] == casillas[8] == player:
    print("Has ganado!!!")
if casillas[2] == casillas[4] == casillas[6] == player:
    print("Has ganado!!!")


if casillas[0] == casillas[1] == casillas[2] == pc:
    print("Has perdido...")
if casillas[3] == casillas[4] == casillas[5] == pc:
    print("Has perdido...")
if casillas[6] == casillas[7] == casillas[8] == pc:
    print("Has perdido...")
if casillas[0] == casillas[3] == casillas[6] == pc:
    print("Has perdido")
if casillas[1] == casillas[4] == casillas[7] == pc:
    print("Has perdido!!!")
if casillas[2] == casillas[5] == casillas[8] == pc:
    print("Has perdido...")
if casillas[0] == casillas[4] == casillas[8] == pc:
    print("Has perdido...")
if casillas[2] == casillas[4] == casillas[6] == pc:
    print("Has perdido...")


print("|"+casillas[0]+"|"+casillas[1]+"|"+casillas[2]+"|")
print("|"+casillas[3]+"|"+casillas[4]+"|"+casillas[5]+"|")
print("|"+casillas[6]+"|"+casillas[7]+"|"+casillas[8]+"|")
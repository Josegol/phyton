from baraja import Baraja
from mano import Mano

mibaraja = Baraja()

mano1 = Mano()

mibaraja.mezclar()

input("Buenas jugador, hoy jugaremos al BlackJack, o más conocido como el 21. ")


cartacogida = mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)
cartacogida = mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)
mano1.mostrar_mano()

mano1.calcula_valor()


if mano1.valor == 21:
    print("Impresionante, la suerte del novato, no está nada mal. ")

while mano1.valor < 21:
   print("Jugador tu puntuación es de ", mano1.valor, "esta bastante bien... ")
   ok = input("¿Quieres seguir jugando, o te conformas? ")
   
   
   if ok == "ok":
    cartacogida = mibaraja.coger_carta()
    mano1.añadir_carta(cartacogida)
    mano1.mostrar_mano()

    mano1.calcula_valor()

    if mano1.valor > 21:
        print("Jugador, te has pasado, si quieres puedes volver a intentarlo. ")


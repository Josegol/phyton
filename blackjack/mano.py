class Mano:

    def __init__(self):
        self.cartas = []
        self.valor = 0

    def añadir_carta(self, carta):
        self.cartas.append(carta)

    def mostrar_mano(self):
        for carta in self.cartas:
            print(carta)
            
    def calcula_valor(self):
        self.valor = 0
        for carta in self.cartas:
            if carta.valor in ["10","Jota","Reina","Rey"]:
               self.valor += 10
            elif carta.valor == "As":
                self.valor += 11
            else:
                self.valor += int(carta.valor)

    
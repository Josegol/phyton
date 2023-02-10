import random

letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
words= ["españa","lluvia","spinosaurus","narval"]
word = random.choice(words)
words_correctas = []
words_incorrectas = []

seguir_jugando = True

while seguir_jugando:
    

    for letra in word:
        if letra in words_correctas:
            print(letra,end="")
        else:
            print("_ ",end="") 
        

    letra_pedida = input("\nDime una letra :) \n")

    print(letra_pedida in word)

    if letra_pedida in word:
        words_correctas.append(letra_pedida)
    else:        
        words_incorrectas.append(letra_pedida)

    print("correctas: ",words_correctas)
    print("incorrectas: ",words_incorrectas)

    if set(words_correctas) == set(word):
        seguir_jugando = False
        print("Has ganado!!!")
    if len(words_incorrectas) == 6:
        seguir_jugando = False
        print("Has perdido...")
        print("La palabra era: ",palabra_secreta)
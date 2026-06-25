# #Con esto realizado, su programa debe simular un juego que permita adivinar el número final
# (ya ajustado). El juego consta de 3 intentos:
# i no se adivina en el primer intento, el programa debe indicar si el número a adivinar
# es mayor o menor.
# • Si aún no se adivina en el segundo intento se debe indicar lo mismo y además dar
# una pista. La pista consiste en decir cuál intento estuvo más.
#  mismo y además dar
# una pista. La pista consiste en decir cuál intento estuvo más cerca
# del número correcto: si el número del primer intento o el del segundo intento
# Si no se adivina en el tercer intento, se debe mostrar el mensaje: "Perdiste." y revelar
# el número.


#EJERCICIO 2


import random

print("Juego de adivinar")

num1 = int(input("Ingresa numero pequeño : "))
num2 = int(input("Ingresa un numero mas grande : "))

intentos = 0
gano = "no"

if num1 >= num2:
    print("Error en el rango.")
else:
    secreto = random.randint(num1, num2)
    
    while intentos < 3 and gano == "no":
        intentos = intentos + 1
        print("Intento:", intentos)
        tiro = int(input("Adivina: "))
        
        if tiro == secreto:
            gano = "si"
        elif tiro < secreto:
            print("Es mayor")
        else:
            print("Es menor")

    if gano == "si":
        print("Ganaste!")
    else:
        print("Perdiste, el numero era:", secreto)

print("Hello")
print("Faure")
# Voici un petit programme de jeu de devinette
# Ecrire par Joseph

import random

print("Bienvenu dans notre programme de devinette")
#devine = random.randint(0,10)
compteur = 0
while True:
    devine = random.randint(0, 10)
    nbre = float(input("Veuillez entrer votre nombre : "))
    if nbre == devine:
        print("Excellent vous avez trouvez le nombre")
        compteur += 1
        break
    elif nbre > devine:

        print("Dommage ! Votre nombre  est trop grand ")
        compteur += 1
    elif nbre < devine :
        print("Dommage ! Votre nombre est trop petit ")
        compteur += 1

print("Le nombre d'essai : ", compteur)

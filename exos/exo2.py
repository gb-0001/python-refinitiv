'''
*** Exo 2 ***
Ecrire un programme python qui propose à l'utilisateur
de deviner un nombre caché (exemple: 560) et
affichera en fonction de la réponse de l'utilisateur:
 - "c'est plus" si le nombre saisi est inférieur au nombre caché
 - "c'est moins" si le nombre saisi est supérieur au nombre caché
Tant que l'utilisateur n'a pas trouvé le nombre caché
on lui demande la saisie
'''
print("*** EXO 2: chiffre mystère à deviner --- version 2 --- ***")

#guessNumber = 560

from random import randint
guessNumber = randint(1, 20)

userNumber = int(input("Essaie de deviner mon chiffre. Saisis un chiffre : "))
while userNumber != guessNumber:
    if userNumber > guessNumber:
        print("C'est moins")
    elif userNumber < guessNumber:
        print("C'est plus")
    userNumber = int(input("Essaie de deviner mon chiffre. Saisis un chiffre : "))

print("Bravo !")
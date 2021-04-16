'''
*** Exo 1 ***
Demander à l'utilisateur de saisir un chiffre
Si le chiffre saisi est supérieur à guess_number
on affiche "c'est moins"
Si le chiffre saisi est inférieur à guess_number
on affiche "c'est plus"
Si le chiffre saisi est égal à guess_number
on affiche "Bravo, tu as deviné !"
'''

guess_number = 42

print("*** EXO 1: chiffre mystère à deviner ***")
player_input = int(input("Saisir un chiffre: "))

if player_input == guess_number:
    print("Bravo, tu as trouvé !")
else:
    if player_input > guess_number:
        print("C'est moins !")
    else:
        print("C'est plus !")
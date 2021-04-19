'''
*** Exo 4: somme de saisies ***
Créer un programme demandant à l'utilisateur se saisir
un chiffre. Tant que l'utilisateur ne saisit pas la valeur "0",
on lui redemande la saisie d'un chiffre.
En sortie de boucle, on affichera la somme des valeurs saisies ainsi qu'un
récapitulatif des valeurs saisies
Ex:
15
2
3
0
=> Somme des valeurs saisies: 20 (15,2,3)
'''
print("*** EXO 4: somme de saisies ***")

#import utils
#from utils import sumList
from utils import sumList as sList

values = []
while True:
  userInput = int(input("Saisir un chiffre (0 pour quitter le programme): "))
  if userInput == 0: # sortie de boucle
    break
  else:
    values.append(userInput) # ajout de la valeur dans la liste

valuesFormatted = '***' + str(values).strip('[]') + '***'
#print("Somme des valeurs saisies:", utils.sumList(values), valuesFormatted)
#print("Somme des valeurs saisies:", sumList(values), valuesFormatted)
print("Somme des valeurs saisies:", sList(values), valuesFormatted)
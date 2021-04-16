# La fonction native input() permet de récupérer une saisie clavier
# input() renvoie une valeur str

'''
print("Quel est votre âge ?")
age = input()
print("Vous avez donc " + age + " ans")
'''

print("Tapez un entier, je calcule son carré")
n = input()
square = int(n) * int(n)
print("Le carré de " + n + " vaut " + str(square))

# alternative syntaxique  1
# conversion implicite de square en str
# possiblité de définir le séparateur de chaîne (argument sep="")
print("Le carré de", n, "vaut", square, sep="  ")

# alernative syntaxique 2
print("Le carré de %s vaut %d" % (n, square))
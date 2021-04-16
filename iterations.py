# les itérations (boucles) consiste à reproduire des instructions
# un certain nombre de fois

# Affichage de "bonjour" sans itération (manuellement)
'''
print("bonjour")
print("bonjour")
print("bonjour")
print("bonjour")
print("bonjour")
'''

count = 0
while count < 5:
    print("bonjour", count)
    # count = count + 1 # incrémentation (augmentation d'une unité)
    count += 1 # alternative syntaxique pour l'incrémentation

count2 = 5
while count2 > 0:
    print("bye", count2)
    count2 -= 1 # décrémentation

# boucle for..in
# range renvoie une liste de 5 éléments
for n in range(5):
    print("Coucou", n)
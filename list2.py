postCodes = [
    67200, 75012, 68520, 15000, 75020,
    67200, 75012, 68520, 15000, 75020,
    67275, 75013, 68600, 17750, 75020,
    75007, 75012, 75520, 15000, 75020
    ]

# Combien de parisiens ?
# 1. variable compteur
# 2. parcourir la liste
# 3. rechercher tout ce qui commence par 75
# 4 .incrémentation de la variable quand c'est trouvé

numParis = 0

for postCode in postCodes:
    # Meilleure approche: opérer sur valeurs numériques
    # if postCode >= 75000 and postCode <= 75999:
    #     numParis += 1

    # Approche par conversion en chaîne (plus coûteuse)
    postCodeStr = str(postCode)
    #dpt = postCodeStr[0] + postCodeStr[1]
    dpt = postCodeStr[:2] # équivalent par slicing
    if dpt == "75":
        numParis += 1

print("Nombre de code postaux parisiens: ", numParis)

# Affichage des 3 dernirs codes postaux de la liste
print(postCodes[-3:])
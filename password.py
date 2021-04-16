goodPassword = "password"
numAttempts = 0
userInput = ""

# boucle tant que le mot de passe est incorrect
# ET que le nombre de tentatives est inférieur à 3
while userInput != goodPassword and numAttempts < 3:
    userInput = input("Votre mot de passe: ")
    numAttempts += 1
    print("Nombre de tentatives", numAttempts)


# Le code suivant est exécutée qu'après la sortie de boucle
if numAttempts == 3 and userInput != goodPassword:
    print("3 mauvaises saisies, compte bloqué")
else:
    print("Connecté")
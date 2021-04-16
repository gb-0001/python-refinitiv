goodPassword = "password"
numAttempts = 0
userInput = ""


# boucle tant que le mot de passe est incorrect
# ET que le nombre de tentatives est inférieur à 3
while userInput != goodPassword and numAttempts < 3:
    userInput = input("Votre mot de passe: ")
    numAttempts += 1 # incrémentation du nombre de tentatives
    print("Nombre de tentatives", numAttempts)


# Le code suivant est exécuté qu'après la sortie de boucle
if userInput != goodPassword:
    print("3 mauvaises saisies, compte bloqué")
else:
    print("Connecté")
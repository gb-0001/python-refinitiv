'''
count = 0
while count < 10:
    print("Hello", count)
    count += 1
    if count == 5:
        break
'''
goodPassword = "password"
numAttempts = 0
userInput = ""

while True:
    userInput = input("Votre mot de passe: ")
    numAttempts += 1

    if userInput == goodPassword:
        print("Connecté, après %d tentatives" % numAttempts)
        break
    
    if numAttempts > 2:
        print("Compte bloqué après %d tentatives" % numAttempts)
        break
    

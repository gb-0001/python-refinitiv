students = [
    "Simon Vincent", 
    "Blanchard Aurélien", 
    "Fourneret Benoît",
    "Abelârd Hétîenne",
    "Pâpâ Noël"
]

# Objectif, construire et afficher les addresses email
# de ces étudiants sous la forme prenom.nom@refinitiv.com

def removeAccents(str):
    newStr = str\
        .replace('é','e')\
        .replace('è','e')\
        .replace('ê','e')\
        .replace('î','i')\
        .replace('à','a')\
        .replace('â','a')\
        .replace('ë','e')
    
    return newStr

#print(removeAccents("élément à demander à l'âme Benoît "))


for student in students:
    # recherche le l'index de l'espace dans la chaîne
    index = student.find(" ") 
    firstName = student[index+1:]
    lastName = student[:index]
    email = firstName + '.' + lastName + '@refinitiv.com'
    #emailFormatted = email.replace("é","e").replace("î","i").lower()
    emailFormatted = removeAccents(email).lower()
    print(emailFormatted)

'''
index = -1
for c in student:
    index += 1
    if c == " ":
        break
print(index)
'''






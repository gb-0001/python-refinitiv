d = {} # dictionary vide

def getAverage(list):
    s = 0 # somme
    for i in list:
        s += i
    return round(s / len(list), 2)

student1 = {
    "lname":"Simon", 
    "fname":"Vincent",
    "email":"vincent.simon@refinitiv.com",
    "isGoodLearner":True,
    "notes":[15, 7, 19.5, 5]
}
student2 = {
    "lname":"Blanchard", 
    "fname":"Aurélien",
    "email":"aurelien.blanchard@refinitiv.com",
    "isGoodLearner":False,
    "notes":[4, 20, 8.5]
}
student3 = {
    "lname":"Fourneret", 
    "fname":"Benoît",
    "email":"benoit.fourneret@refinitiv.com",
    "isGoodLearner":True,
    "notes":[15, 2, 18]
}

# print(student1)
# print(student1["lname"])

students = [student1, student2, student3]

for s in students:
    if s["isGoodLearner"]:
        evaluation = "est un bon étudiant"
    else:
        evaluation = "est mauvais étudiant"

    print(s["fname"], evaluation, "Moyenne:", getAverage(s["notes"]))

# dans la boucle ci-dessus
# afficher la moyenne des notes obtenues par l'étudiant
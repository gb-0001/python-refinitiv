student = {
  "fname": "Chris",
  "lname": "DUFOUR",
  "isGoodLearner": True
}
print(student)

# ajout d'une nouvelle clé
student["notes"] = [14,6,20] 
print(student)

# modification multi-clés
student.update({"fname":"Christophe", "lname": "Dufour"})
print(student)

# suppression d'une clé (notes)
student.pop("notes")
print(student)
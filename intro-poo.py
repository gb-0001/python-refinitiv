class Student:
  # propriétés
  fname = ''
  lname = ''

  # méthodes
  def getFirstName(self):
    return self.fname

# instanciation de la classe Student
# production d'un objet objet de type Student
student1 = Student()
student2 = Student()
student3 = Student()

student1.fname = "Chris"
student2.fname = "Vincent"
student3.fname = "Aurélien"

students = [student1, student2, student3]

for s in students:
  print(s.getFirstName())
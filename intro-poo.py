class Student:
  # propriétés (variables déclarées dans une classe)
  fname = ''
  lname = ''

  # méthodes (fonctionas déclarées dans une classe)
  def getFirstName(self):
    return self.fname

  def getLastName(self):
    return self.lname

  def getFullName(self):
    return self.fname + ' ' + self.lname

  def getInitials(self):
    return self.fname[:1] + self.lname[:1]







# instanciation de la classe Student
# production d'un objet objet de type Student
student1 = Student()
student2 = Student()
student3 = Student()

student1.fname = "Chris"
student1.lname = "Dufour"

student2.fname = "Vincent"
student2.lname = "Simon"

student3.fname = "Aurélien"
student3.lname = "Blanchard"

students = [student1, student2, student3]

for s in students:
  print(s.getFullName(), s.getInitials())
import csv

# production d'un fichier CSV
with open('files/students.csv', mode='w', newline='') as csv_file:
  writer = csv.writer(csv_file, delimiter=',', quotechar='*')
  writer.writerow(['Nom', 'Poste', 'Ville'])
  writer.writerow(['Chris, Dufour', 'Dev', 'Strasbourg'])
  writer.writerow(['Toto Truc', 'Data scientist', 'Paris'])
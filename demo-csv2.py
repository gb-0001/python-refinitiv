import csv # module natif => https://docs.python.org/3/library/csv.html#module-csv

#csv_file = open('files/cities.csv')
with open('files/cities.csv', 'r') as csv_file:
  rows = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for r in rows:
    if line_count == 0:
      # ligne d'entête
      print(f'Colonnes: {", ".join(r)}')
    else:
      print(f'{r[8]}: {r[0].strip()}° {r[1].strip()}')
    line_count += 1

print(f'[+] {line_count} lignes traitées.')
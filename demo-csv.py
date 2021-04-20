f = open('files/cities.csv', 'r')
content = f.read()
f.close()
#print(type(content)) # <class 'str'>
rows = content.splitlines() # liste de lignes
#print(len(rows)) # 129

latDIndex = 0
latMIndex = 1
cityNameIndex = 8
for r in rows:
  cols = r.split(',') # virgule = caractère de séparation
  # le premier strip suprime les spaces avant/arrière
  # le second supprimer les doubles guillemets
  cityName = cols[cityNameIndex].strip().strip('"')
  if cityName.startswith('San'):
    print(f'{cityName}: {cols[latDIndex].strip()}° {cols[latMIndex].strip()}')
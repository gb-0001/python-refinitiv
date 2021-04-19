fileNames = ['chris','vincent','aurelien','benoit']

content = 'Fichier texte appartenant à '

for n in fileNames:
  fName = 'files/demo_' + n + '.txt' # création du nom de fichier
  f = open(fName, 'w')
  f.write(content + n.upper())
  f.close()
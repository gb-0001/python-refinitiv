import os

#os.mkdir('blabla') # crée dossier
#os.rmdir('blabla') # supprimer dossier
# if os.path.exists('blabla'):
#   print("Le dossier blabla existe déjà")

if not os.path.exists('files/students'):
  os.mkdir('files/students')

for f in os.listdir('files'):
  if f.startswith('demo_'):
    os.rename('files/' + f, 'files/students/' + f)
    print("[+] fichier %s déplacé" % f)
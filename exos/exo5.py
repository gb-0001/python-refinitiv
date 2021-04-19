'''
*** Exo 5: flags => flagsBis ***
Créer un programme qui produira un dossier flagsBis
Ce dossier contiendra tous les fichier png d'origine mais
renommés en ne conservant que les deux premières lettres.
Ces lettres seront en masjuscule.
ex: 
  exos/flags/allemagne.png => exos/flagsBis/AL.png
  exos/flags/belgique.png => exos/flagsBis/BE.png

Le fichier missing.png devra être ignoré
'''
print("*** EXO 5: flags => flagsBis ***")

import os
import shutil


if not os.path.exists('flagsBis'):
  os.mkdir('flagsBis')

# parcours des drapeaux d'origine
for f in os.listdir('flags'):
  if not f == 'missing.png':
    shutil.copyfile('flags/' + f, 'flagsBis/' + f[:2].upper() + '.png')
    print("[+] drapeau %s copié et renommé" % f)


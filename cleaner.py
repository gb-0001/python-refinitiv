import os

#os.remove('files/new.txt')
files = os.listdir('files')

nbDeletedFiles = 0
for f in files:
  if f[:5] == 'demo_':
    os.remove('files/' + f)
    print('[-] fichier %s supprimé' % f)
    nbDeletedFiles += 1

print('\n') # saut de ligne
print('[-] %d fichiers supprimés' % nbDeletedFiles)

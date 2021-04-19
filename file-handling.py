f = open('files/demo.txt', 'r')
content = f.read() # renvoie str
f.close()

newContent = content.replace('demo', 'preuve')

print(content)
print(newContent)

nf = open('files/new.txt', 'w')
nf.write(newContent)
nf.close() # fermeture explicite pour "libérer" la ressource
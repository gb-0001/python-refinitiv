from random import randint

proverbs = [
  'Pierre qui roule n\'amasse plas mousse',
  'Il ne faut pas vendre la peau de l\'ours',
  'Tra il dire e il fare c\'e in mezzo il mare',
  'Ad astra per aspera'
]

# affichage d'un proverbe par index aléatoire
indexMax = len(proverbs)-1
print(proverbs[randint(0,indexMax)])
# Variables primitives en Python
training = "Initiation Python"
temperature = 15
pi = 3.14
isEarthRound = True

print(type(training)) # str
print(type(temperature)) # int
print(type(pi)) # float
print(type(isEarthRound)) # bool

'''
# Block comment
print(2+2)
print(training)

training = "Perfectionnement JavaScript"
print(training)
'''

# Opération sur variables
print(temperature + 10) # addition
print(training + " 10") # concaténation (réunion de plusieurs chaînes)
print(pi + 10)
print(isEarthRound + 10) # 11

print("Le double de pi est: " + str(pi * 2))

doublePi = pi * 2
doublePiStr = str(doublePi) # conversion en string d'une variable float
print("Le double de pi est: " + doublePiStr)
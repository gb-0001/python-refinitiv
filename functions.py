# une fonction est un ensemble d'instructions
# que l'on peut exécuter autant de fois que souhaité

def hello():
    print("Hello !")
    return None

def hello2():
    return "Hello2 !"

def addTwo(n):
    return n + 2

def square(n):
    return n * n

# demo = hello()
# print(demo)
#print(hello2())

# print(addTwo(4))
# print(addTwo(400))
# print(addTwo(14))

# print(square(5))
# print(square(6) * 2)
# print(square(3) + square(4))

numbers = [6,4,10,8,15]
for n in numbers:
    print(square(n))





# liste de 3 entiers
numbers = [23,140,6]
#print(type(numbers)) # <class 'list'>

# for number in numbers:
#     print(number)

first = numbers[0]
computedIndex = 1 + 1
#print(numbers[computedIndex])

# index = 0
# while index < 3:
#     print(numbers[index])
#     index += 1

title = "Les trois Mousquetaires"
#print(title[4])
numE = 0
searchedChar = "i"
for char in title:
    if char == searchedChar:
        numE += 1

print("Le caractère %s a été trouvée %d fois dans le titre %s" 
    % (searchedChar, numE, title))
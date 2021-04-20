'''
*** Exo 3 ***
Créer un programme demandant à l'utilisateur se saisir
un taux de tva (ex: 20, ou 5.5)
Calculer et afficher le prix TTC de tous les prix
contenus dans la variable "prices" sur la base du taux
fourni par l'utilisateur
'''
def getPriceWithVAT(price, vat, shouldRound=True):
    priceWithVat = price * (1 + vat/100)
    if shouldRound:
        return round(priceWithVat, 2)
    else:
        return priceWithVat

prices = [14,100,30,10,8]

userVat = float(input("TVA: "))
for p in prices:
    print(getPriceWithVAT(p, userVat, shouldRound=False))
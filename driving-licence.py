age = int(input("Veuillez saisir votre âge: "))

if age >= 18:
    print("Vous avez le droit de conduire")
else:
    if age >= 16:
        print("Conduite acc. possible")
    else:
        print("Conduite pas possible")
        print("Tu devras attendre", 16-age, "an(s)")

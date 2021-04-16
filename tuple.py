#t = (); # tuple vide

# coordGps = (45.9632, 21.7891)
# print(coordGps)
# print("Latitude:", coordGps[0])
# print("Longitude:", coordGps[1])

# lat, lng = coordGps # tuple unpacked
# print(lat, lng)

def getGpsCoords(cityName):
    # Appel à un service/API de geolocalisation
    # ex: Google Maps
    if cityName == "Paris":
        return (48.8534, 2.3488)
    elif cityName == "Strasbourg":
        return (48.5833, 7.75)
    else:
        return None

lat, lng = getGpsCoords("Paris")
print("Latitude:", lat, "Longitude", lng)

client = ("Chris", "Dufour", "Strasbourg", "Dev")
fname, lastname, city, job = client
print(job)

listCoords = [
    (48.8534, 2.3488),
    (48.5833, 7.75),
    (43.2964, 5.3697)
]

for c in listCoords:
    lat, lng = c
    print("Latitude:", lat, "Longitude", lng)
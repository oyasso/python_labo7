import json
import sys


server_lijst = []
with open("serverlijst.json", "r") as j:
    server_lijst = json.load(j)

if len(sys.argv) < 2:
    print("Welkom bij de server manager\n")
    print("Kies een van de drie opties\n\n")
    keuze = input("1. Server toevoegen\n2. Server verwijderen\n\
3. Serverlijst tonen\n\n")

    if (keuze == "1"):
        server_naam = input("Welke server wil je toevoegen?\n")
        server_lijst.append(server_naam)
    elif (keuze == "2"):
        server_naam = input("Welke server wil je verwijderen?\n")
        server_lijst.remove(server_naam)
    elif (keuze == "3"):
        for server in server_lijst:
            print(server)
    else:
        print("Dit is geen geldige keuze")
else:
    if sys.argv[1] == "add":
        server_lijst.append(sys.argv[2])
    elif sys.argv[1] == "remove":
        server_lijst.remove(sys.argv[2])
    elif sys.argv[1] == "show":
        for server in server_lijst:
            print(server)

with open("serverlijst.json", "w") as j:
    json.dump(server_lijst, j)

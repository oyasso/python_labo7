import json
import sys
import platform
import subprocess


def add_server(naam, list):
    """toevoegen van een genoemde server"""
    list.append(naam)


def remove_server(naam, list):
    """verwijderen van een genoemde server"""
    list.remove(naam)


def show_servers(list):
    """toont de huidige servers in de lijst"""
    for item in list:
        print(item)


def myping(host):
    parameter = "-n" if platform.system().lower() == "windows" else '-c'
    command = ['ping', parameter, "4", host]
    response = subprocess.call(command)
    if response == 0:
        return True
    else:
        return False


def main():
    # management modus
    server_lijst = []
    with open("serverlijst.json", "r") as j:
        server_lijst = json.load(j)

    if len(sys.argv) < 2:
        print("Welkom bij de server manager\n")
        print("Kies een van de drie opties\n\n")
        keuze = input("1. Server toevoegen\n2. Server verwijderen\n\
3. Serverlijst tonen\n\n")

        if (keuze == "1"):
            add_server(input("Welke server toevoegen?\n"), server_lijst)
        elif (keuze == "2"):
            remove_server(input("Welke server verwijderen?\n"), server_lijst)
        elif (keuze == "3"):
            show_servers(server_lijst)
        else:
            print("Dit is geen geldige keuze")
    elif sys.argv[1] == "manage":
        if sys.argv[2] == "add":
            add_server(sys.argv[3], server_lijst)
        elif sys.argv[2] == "remove":
            remove_server(sys.argv[3], server_lijst)
        elif sys.argv[2] == "show":
            show_servers(server_lijst)

    with open("serverlijst.json", "w") as j:
        json.dump(server_lijst, j)

    # check modus
    if sys.argv[1] == "check":
        result = print(myping(sys.argv[2]))

        with open("pingresults.json", "w") as p:
            json.dump(result, p)


if __name__ == "__main__":
    main()

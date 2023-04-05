import json
import sys
from ping3 import ping


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


def myping3(host):
    """check if server is online"""
    if ping(host) is False:
        return "Server offline"
    else:
        return "Server online"


def main():
    servernames_and_status = []
    server_lijst = []  # maak een lijst met servers
    # open json files
    with open("serverlijst.json", "r") as j:
        server_lijst = json.load(j)
    with open("pingresults.json", "r") as p:
        servernames_and_status = json.load(p)

    # management modus
    # terminal interactive interface
    if len(sys.argv) < 2:
        print("Welkom bij de server manager\n")
        print("Kies een van de drie opties\n\n")
        keuze = input("1. Server toevoegen\n2. Server verwijderen\n\
3. Serverlijst tonen\n4. Server pingen\n\n")

        if (keuze == "1"):
            add_server(input("Welke server toevoegen?\n"), server_lijst)
        elif (keuze == "2"):
            remove_server(input("Welke server verwijderen?\n"), server_lijst)
        elif (keuze == "3"):
            show_servers(server_lijst)
        elif (keuze == "4"):
            server_to_ping = input("Welke server wil je pingen?\n")
            server_status = myping3(server_to_ping)
            print(server_status)
            servernames_and_status.append({server_to_ping: server_status})
            with open("pingresults.json", "w") as p:
                json.dump(servernames_and_status, p)
        else:
            print("Dit is geen geldige keuze")
    # command-line arguments
    elif sys.argv[1] == "manage":
        if sys.argv[2] == "add":
            add_server(sys.argv[3], server_lijst)
        elif sys.argv[2] == "remove":
            remove_server(sys.argv[3], server_lijst)
        elif sys.argv[2] == "show":
            show_servers(server_lijst)

    # check modus
    elif sys.argv[1] == "check":
        server_to_ping = sys.argv[2]
        server_status = myping3(server_to_ping)
        print(server_status)
        servernames_and_status.append({server_to_ping: server_status})
        with open("pingresults.json", "w") as p:
            json.dump(servernames_and_status, p)

    with open("serverlijst.json", "w") as j:
        json.dump(server_lijst, j)


if __name__ == "__main__":
    main()

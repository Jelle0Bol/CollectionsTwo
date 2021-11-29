import sys


def boodschappenlijstje():
    while True:
        print()
        print("### Boodschappenlijstje ###")

        print()
        print("1) Iets toevoegen aan het lijstje")
        print("2) Totale lijstje tonen")
        print("3) Iets verwijderen van het lijstje")
        print("4) Afsluiten")
        print()

        selection = input("Kies uit de volgende mogelijkheden : ")

        if selection == "1":
            addItem()
        elif selection == "2":
            showBoodschappen()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            sys.exit()
        else:
            ("Dat is geen geldige keuze. Kies uit 1, 2 of 3 ")

boodschappenList = []

def showBoodschappen():
    print()
    print("--- BOODSCHAPPENLIJSTJE ---")
    for i in boodschappenList:
        print("* " + i)

def addItem():
    item = input("Typ je item die je wilt toevoegen in het boodschappenlijstje hier : ")
    boodschappenList.append(item)
    print()
    print(item + " is toegevoegd aan het boodschappenlijstje")

def removeItem():
    item = input("Typ je item die je wilt weghalen van het boodschappenlijstje : ")
    boodschappenList.remove(item)
    print()
    print(item + " is weggehaald van het boodschappenlijstje")

boodschappenlijstje()
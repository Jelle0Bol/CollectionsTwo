# Lootjes Test

# Maak een list waarbij namen worden toegevoegd!
# Geen zelfde naam!
# Werkt alleen bij 2 of meer namen!
# Voor alle namen een lootje!
# Iedereen heeft een uniek lootje
# Niemand mag een lootje van zichzelf hebben
# Print de lijst met de namen van de getrokken personen

import sys
sys.setrecursionlimit(10000)
from typing import Set
import random

namenlootje = []
namenlootje2 = []
minimaal = 0
compleetlootje = []
compleetlootje2 = []
som = 0

def loting():
    x=0
    random.shuffle(namenlootje)
    while x <= len(namenlootje):
        randompersoon1 = random.choice(namenlootje)
        randompersoon2 = random.choice(namenlootje2)
        if randompersoon1 == randompersoon2:
            loting()
        else:
            if randompersoon1 in compleetlootje or randompersoon2 in compleetlootje2:
                loting()
            else:
                compleetlootje.append(randompersoon1)
                compleetlootje2.append(randompersoon2)
                print(randompersoon1 + "-" + randompersoon2)
                x+=1


def lootjesDoorgaan():
    global doorgaanMetLootjes
    doorgaanMetLootjes = input("Wil je doorgaan met namen doorgeven voor in het lijstje? Y / N : ").lower()
    if doorgaanMetLootjes == "y":
        lootjesOpnieuw()
    elif doorgaanMetLootjes == "n":
        print("Dit zijn de namen die je hebt voor de loten : ")
        print(namenlootje)
        for p in range(1):
            loting()
    else:
        print ("Geef alleen 'Y' of 'N' door")
        lootjesDoorgaan()

def lootjesOpnieuw():
    xcx = input("Welke naam wil je toevoegen voor de loting? : ")
    if xcx in namenlootje:
        print("Deze naam zit al in de lijst")
        lootjesOpnieuw()
    else:
        namenlootje.append(xcx)
        namenlootje2.append(xcx)
        print("Dit zijn de namen in je loting : ")
        print(namenlootje)
        xax = input("Wil je nog een naam toevoegen? Y/N : ").lower()
        if xax == "y":
            lootjesOpnieuw()
        elif xax == "n":
                loting()
        else:
            print("Beantwoord alleen met 'Y' of 'N'")
            lootjesOpnieuw()

while minimaal <= 1:
    namenVoorList = input("Welke namen wil je in de list zetten? Minimaal 2! : ")
    if namenVoorList in namenlootje:
        print("Deze naam zit al in de list")
        lootjesOpnieuw()
    else:
        namenlootje.append(namenVoorList)
        namenlootje2.append(namenVoorList)
        print("Dit zijn de namen die je nu in je lijstje hebt : ")
        print(namenlootje)
        minimaal += 1



lootjesDoorgaan()
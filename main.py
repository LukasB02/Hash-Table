import hashtable
import stock
import plot
from csv_import import read_csv

table = [None] * 2003

print("COMMANDS: ADD/DEL/IMPORT/SEARCH/LOAD/SAVE/PLOT/QUIT")

while True:
    userInput = input("Eingabe: ")

    if userInput == "ADD":
        name = input("Aktienname: ")
        wkn = input("Aktienwkn: ")
        symbol = input("Aktiensymbol: ")

        hashtable.add(table, stock.stock(name, wkn, symbol))
        print("Aktie wurde hinzugefügt")

    elif userInput == "DEL":
        name = input("Aktienname: ")

        hashtable.delete(table, name)

    elif userInput == "IMPORT":
        name = input("Aktienname: ")
        filepath = input("Aktienfilepath: ")

        if hashtable.search(table, name):
            table[hashtable.getindex(table, name)] = read_csv(filepath, name)

    elif userInput == "SEARCH":
        nameORsymbol = input("Aktienname/Aktiensymbol: ")

        if hashtable.search(table, nameORsymbol):
            hashtable.printnewest(table, nameORsymbol)

    elif userInput == "LOAD":
        print("LOAD")

    elif userInput == "SAVE":
        print("SAVE")

    elif userInput == "PLOT":
        name = input("Aktienname: ")
        if hashtable.search(table, name):
            plot.plot(table[hashtable.getindex(table, name)]["prices"])

    elif userInput == "QUIT":
        break






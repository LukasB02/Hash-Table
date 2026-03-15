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
        print("Aktie wurde hinzugefügt.")

    elif userInput == "DEL":
        print("DEL")

    elif userInput == "IMPORT":
        filepath = input("Aktienfilepath: ")
        name = input("Aktienname: ")

        if hashtable.search(table, name):
            table[hashtable.getindex(table, name)] = read_csv(filepath, name)

    elif userInput == "SEARCH":
        nameORsymbol = input("Aktienname/Aktiensymbol: ")

        print(hashtable.search(table, nameORsymbol))
    elif userInput == "LOAD":
        print("LOAD")

    elif userInput == "SAVE":
        print("SAVE")

    elif userInput == "PLOT":
        nameORsymbol = input("Aktienname/Aktiensymbol: ")
        for entry in table:
            if entry is not None and (entry["name"] == nameORsymbol or entry["symbol"] == nameORsymbol):
                plot.plot(entry["prices"])
                break

    elif userInput == "QUIT":
        break






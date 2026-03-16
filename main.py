import hashtable
import stock
import plot
import loadsave
from csv_import import read_csv

table = [None] * 2003

print("COMMANDS: ADD/DEL/IMPORT/SEARCH/LOAD/SAVE/PLOT/QUIT")

while True:
    userInput = input("Eingabe: ")

    if userInput == "ADD":
        name = input("Aktienname: ")
        wkn = input("Aktienwkn: ")
        symbol = input("Aktiensymbol: ")

        if not hashtable.search(table, name):
            hashtable.add(table, stock.stock(name, wkn, symbol))
            print("Aktie wurde hinzugefügt")
        else:
            print("Aktie existiert schon")

    elif userInput == "DEL":
        name = input("Aktienname: ")

        if hashtable.search(table, name):
            hashtable.delete(table, name)
            print("Aktie wurde gelöscht")
        else:
            print("Aktie wurde nicht gefunden")

    elif userInput == "IMPORT":
        name = input("Aktienname: ")

        if hashtable.search(table, name):
            filepath = input("Aktienfilepath: ")
            table[hashtable.getindex(table, name)] = read_csv(filepath, name)
        else:
            print("Aktie wurde nicht gefunden")

    elif userInput == "SEARCH":
        nameORsymbol = input("Aktienname/Aktiensymbol: ")

        if hashtable.search(table, nameORsymbol):
            hashtable.printnewest(table, nameORsymbol)
        else:
            print("Aktie wurde nicht gefunden")

    elif userInput == "LOAD":
        filename = input("Dateiname: ")
        table = loadsave.load_stocks(filename)

    elif userInput == "SAVE":
        filename = input("Dateiname: ")
        loadsave.save_stocks(table, filename)

    elif userInput == "PLOT":
        name = input("Aktienname: ")

        if hashtable.search(table, name):
            plot.plot(table[hashtable.getindex(table, name)]["prices"])
        else:
            print("Aktie wurde nicht gefunden")

    elif userInput == "QUIT":
        break






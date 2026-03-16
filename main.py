import hashtable
import stock
import plot
import loadsave
from csv_import import read_csv

table = [None] * 2003

print("COMMANDS: ADD/DEL/IMPORT/SEARCH/LOAD/SAVE/PLOT/QUIT")

while True: #Ends when the user inputs QUIT
    userInput = input("Eingabe: ")  #User Input

    if userInput == "ADD":
        name = input("Aktienname: ")
        wkn = input("Aktienwkn: ")
        symbol = input("Aktiensymbol: ")

        hashtable.add(table, stock.stock(name, wkn, symbol))

    elif userInput == "DEL":
        name = input("Aktienname: ")
        hashtable.delete(table, name)

    elif userInput == "IMPORT":
        name = input("Aktienname: ")

        if hashtable.search(table, name):   #Checks if the stock exists
            filepath = input("Aktienfilepath: ")
            table[hashtable.getindex(table, name)] = read_csv(filepath, name)
        else:
            print("Aktie wurde nicht gefunden")

    elif userInput == "SEARCH":
        nameORsymbol = input("Aktienname/Aktiensymbol: ")
        hashtable.printnewest(table, nameORsymbol)

    elif userInput == "LOAD":
        filename = input("Dateiname: ")
        table = loadsave.load_stocks(filename)

    elif userInput == "SAVE":
        filename = input("Dateiname: ")
        loadsave.save_stocks(table, filename)

    elif userInput == "PLOT":
        name = input("Aktienname: ")

        if hashtable.search(table, name):   #Checks if the stock exists
            plot.plot(table[hashtable.getindex(table, name)]["prices"])
        else:
            print("Aktie wurde nicht gefunden")

    elif userInput == "QUIT":
        break






import hashtable
import stock
import plot

table = [None] * 2003

while True:
    userInput = input()

    if userInput == "ADD":
        name = input("Aktienname: ")
        wkn = input("Aktienwkn: ")
        symbol = input("Aktiensymbol: ")

        hashtable.add(table, stock.Stock(name, wkn, symbol))
    elif userInput == "DEL":
        print("DEL")
    elif userInput == "IMPORT":
        print("IMPORT")
    elif userInput == "SEARCH":
        nameORsymbol = input("Aktienname/Aktiensymbol: ")

        print(hashtable.search(table, nameORsymbol))
    elif userInput == "LOAD":
        print("LOAD")
    elif userInput == "SAVE":
        print("SAVE")
    elif userInput == "PLOT":
        plot.plot(table)
    elif userInput == "TEST":
        print(hash)
    elif userInput == "QUIT":
        break





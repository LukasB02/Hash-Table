import hashtable

hash = hashtable.hash("Apple")

while True:
    userInput = input()

    if(userInput == "ADD"):
        print("ADD")
    elif(userInput == "DEL"):
        print("DEL")
    elif(userInput == "IMPORT"):
        print("IMPORT")
    elif(userInput == "SEARCH"):
        print("SEARCH")
    elif(userInput == "LOAD"):
        print("LOAD")
    elif(userInput == "SAVE"):
        print("SAVE")
    elif(userInput == "TEST"):
        print(hash)
    elif(userInput == "QUIT"):
        break





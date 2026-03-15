import hashtable
import json
import os

#directory for saving and loading the json files
DATA_DIR = "./data/"

def save_stocks(table, filename):
    
    filepath = DATA_DIR + filename
    
    #check if file already exists
    if os.path.exists(filepath):
        print(f"Fehler: Datei '{filename}' existiert bereits!")
        return
    
    #only save the slots in the table that are not None (that contain stocks)
    stocks = []
    for slot in table:
        if slot is not None:
            stocks.append(slot)

    #write the stocks into a json file in the data directory
    with open(filepath, 'w') as jsonfile:
        json.dump(stocks, jsonfile, indent=2)


def load_stocks(filename):

    #open json file and save the stocks into a list
    filepath = DATA_DIR + filename
    with open(filepath, 'r') as jsonfile:
        stocks = json.load(jsonfile)

    #create a new hash table
    table = [None] * 2003

    #add the stocks from the list into the hash table
    for stock in stocks:
        hashtable.add(table, stock)

    return table

import hashtable
import json

def save_stocks(table, filename):
    
    #only save the slots in the table that are not None (that contain stocks)
    stocks = []
    for slot in table:
        if slot is not None:
            stocks.append(slot)

    #write the stocks into a json file
    with open(filename, 'w') as jsonfile:
        json.dump(stocks, jsonfile, indent=2)


def load_stocks(filename):

    #open json file and save the stocks into a list
    with open(filename, 'r') as jsonfile:
        stocks = json.load(jsonfile)

    #create a new hash table
    table = [None] * 2003

    #add the stocks from the list into the hash table
    for stock in stocks:
        hashtable.add(table, stock)

    return table

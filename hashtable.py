def hash(key):  #hashes a string into an index
    h = 0
    for char in key:
        h = (h * 31 + ord(char)) % 2003 #hashfunction with table size 2003
    return h

def add(table, stock):  #creates a new stock dictionary
    h = hash(stock["name"])

    if not search(table, stock):  # Checks if the stock already exists
        print("Aktie wurde hinzugefügt")
        table[getindex(table, stock)] = stock
    else:
        print("Aktie existiert schon")
        return

def getindex(table, stock): #returns the index of a stock
    h = hash(stock)

    for i in range(2003):   #goes through all indexes
        index = (h + i * i) % 2003  #quadratic probing
        if table[index] is not None:
            if table[index]["name"] == stock:
                return index
    return None

def delete(table, stock):   #delets a stock
    h = hash(stock)

    if search(table, stock):  # Checks if the stock exists
        print("Aktie wurde gelöscht")
        table[getindex(table, stock)] = None
    else:
        print("Aktie wurde nicht gefunden")
        return

def search(table, stock):   #outputs TRUE if the stock exists
    h = hash(stock)

    for i in range(2003):   #goes through all indexes
        index = (h + i*i) % 2003    #quadratic probing
        if table[index] is not None:
            if table[index]["name"] == stock:
                return True
    for entry in table: #incase no name was found, go through all entries and search for the symbol
        if entry is not None and entry["symbol"] == stock:
            return True

    return False

def printnewest(table, stock):  #prints the newest stock prices
    if not search(table, stock):  # Checks if the stock exists
        print("Aktie wurde nicht gefunden")
        return

    prices = table[getindex(table, stock)]["prices"]    #gets all prices stored from a specific stock

    newest = prices[-1]

    print(f"Date:   {newest['date']}")
    print(f"Close:  {newest['close']}")
    print(f"Volume: {newest['volume']}")
    print(f"Open:   {newest['open']}")
    print(f"High:   {newest['high']}")
    print(f"Low:    {newest['low']}")

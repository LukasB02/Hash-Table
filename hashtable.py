def hash(key):  #hashes a string into an index
    h = 0
    for char in key:
        h = (h * 31 + ord(char)) % 2003 #hashfunction with table size 2003
    return h

def add(table, stock):  #creates a new stock dictionary
    if not search(table, stock["name"]):  # Checks if the stock already exists
        print("Aktie wurde hinzugefügt")
        table[hash(stock["name"])] = stock  #Adds the stock at the right index
    else:
        print("Aktie existiert schon")
        return

def getindex(table, stockname): #returns the index of a stock
    h = hash(stockname)

    for i in range(2003):   #goes through all indexes
        index = (h + i * i) % 2003  #quadratic probing
        if table[index] is not None:
            if table[index]["name"] == stockname:
                return index
    return None

def delete(table, stockname):   #delets a stock
    if search(table, stockname):  # Checks if the stock exists
        print("Aktie wurde gelöscht")
        table[getindex(table, stockname)] = None
    else:
        print("Aktie wurde nicht gefunden")
        return

def search(table, stockname):   #outputs TRUE if the stock exists
    h = hash(stockname)

    for i in range(2003):   #goes through all indexes
        index = (h + i*i) % 2003    #quadratic probing
        if table[index] is not None:
            if table[index]["name"] == stockname:
                return True
    for entry in table: #incase no name was found, go through all entries and search for the symbol
        if entry is not None and entry["symbol"] == stockname:
            return True

    return False

def printnewest(table, stockname):  #prints the newest stock prices
    if not search(table, stockname):  # Checks if the stock exists
        print("Aktie wurde nicht gefunden")
        return

    prices = table[getindex(table, stockname)]["prices"]    #gets all prices stored from a specific stock

    if len(prices) > 0:
        newest = prices[-1]

        print(f"Date:   {newest['date']}")
        print(f"Close:  {newest['close']}")
        print(f"Volume: {newest['volume']}")
        print(f"Open:   {newest['open']}")
        print(f"High:   {newest['high']}")
        print(f"Low:    {newest['low']}")
    else:
        print("Keine Kurseinträge für diese Aktie gefunden")
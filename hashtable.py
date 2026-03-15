def hash(key):
    h = 0
    for char in key:
        h = (h * 31 + ord(char)) % 2003
    return h

def add(table, stock):
    h = hash(stock["name"])

    for i in range(2003):
        index = (h + i*i) % 2003
        if table[index] is None:
            table[index] = stock
            return

def delete(table, stock):
    h = hash(stock["name"])

    for i in range(2003):
        index = (h + i*i) % 2003
        if table[index] is None:
            return  "stock not found"
        if table[index]["name"] == stock["name"]:
            table[index] = None
            return

def search(table, stock):
    h = hash(stock)

    for i in range(2003):
        index = (h + i*i) % 2003
        if table[index] is not None:
            if table[index]["name"] == stock or table[index]["symbol"] == stock:
                return "found"
    for entry in table:
        if entry is not None and entry["symbol"] == stock:
            return "found"

    return "not found"

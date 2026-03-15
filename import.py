import csv
from price import price
from stock import stock

from datetime import datetime



def read_csv(filepath, name):

    Stock = stock(name = name, wkn="", symbol="") #create a new stock object with the given name

    with open(filepath, 'r') as file:
        reader = csv.reader(file)

        next(reader) #skip the header row
        
        for row in reader:
            date = row[0]
            close = float(row[1].replace('$', '')) #remove the $ sign so convert to float works
            volume = int(row[2])
            open = float(row[3].replace('$', ''))
            high = float(row[4].replace('$', ''))
            low = float(row[5].replace('$', ''))

            price_data = price(date, close, volume, open, high, low) #create a price data dictionary

            Stock["prices"].append(price_data) #add the price data to the stock object

    Stock["prices"].sort(key=lambda p: datetime.strptime(p['date'], '%m/%d/%Y') )

    if len(Stock["prices"]) > 30: #if there are more than 30 price entries only keep the most recent 30
        Stock["prices"] = Stock["prices"][-30:]

    return Stock
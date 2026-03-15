import csv
from price import price
from stock import Stock



def read_csv(filepath, name):

    stock = Stock(name = name) #create a new stock object with the given name

    with open(filepath, 'r') as file:
        reader = csv.reader(file)

        next(reader) #skip the header row
        
        for row in reader:
            date = row[0]
            close = float(row[1].replace('$', '')) #remove the $ sign so convert to float works
            volume = int(row[2])
            open_ = float(row[3].replace('$', ''))
            high = float(row[4].replace('$', ''))
            low = float(row[5].replace('$', ''))

            price_data = price(date, close, volume, open_, high, low) #create a price data dictionary

            stock.add_price(price_data) #add the price data to the stock object


    return stock
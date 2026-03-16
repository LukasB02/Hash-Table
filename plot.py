def plot(prices):
    prices = [p["close"] for p in prices[-30:]]
    low = min(prices)
    high = max(prices)
    diff = high - low
    middle = (low + high) / 2
    row = diff / 10

    print("Highest Price: ", high, "Lowest Price: ", low)

    for i in range(10):
        level = high - (row * i)
        print("           |", end="")

        for p in prices:
            if level <= p < level + row:
                print("*", end="")
            else:
                print(" ", end="")
        print()



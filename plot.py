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
        if i==0:
            print(f"{high:6.2f} |", end="")
        elif i == 5:
            print(f"{middle:6.2f} |", end="")
        elif i == 9:
            print(f"{low:6.2f} |", end="")
        else:
            print("           |", end="")

        for p in prices:
            if level <= p < level + row:
                print("*", end="")
            else:
                print(" ", end="")
        print()
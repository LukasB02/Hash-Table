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

        if i == 5:
            print(f"{middle:6.2f} |", end="")
        elif i == 9:
            print(f"{low:6.2f} |", end="")
        else:
            print("       |", end="")

        for j in range(len(prices) - 1):
            today = prices[j]
            tomorrow = prices[j + 1]

            if level <= today < level + row:
                if tomorrow > today:
                    print("/", end="")
                elif tomorrow < today:
                    print("\\", end="")
                else:
                    print("_", end="")
            elif (today < level <= tomorrow) or (tomorrow < level <= today):
                print("|", end="")
            else:
                print(" ", end="")
        print()
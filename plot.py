import price
#def plot(prices):
#    prices = [p["close"] for p in prices[-30:]]
#
#    low = min(prices)
#    high = max(prices)
#    diff = high - low
#    middle = (low + high) / 2
#    row = diff / 10
#
#    print("Highest Price: ", high, "Lowest Price: ", low)
#
#    print(f"{high: 6.2f} |", end="") #print high, low and median price left of
#
#    for i in range(10):
#        level = high - (row * i)
#
#        if i == 5:
#            print(f"{middle:6.2f} |", end="")
#        elif i == 9:
#            print(f"{low:6.2f} |", end="")
#        else:
#            print("            |", end="")
#
#        for j in range(len(prices) - 1):
#            today = prices[j]
#            tomorrow = prices[j + 1]
#
#            jump = tomorrow - today
#
#            if level <= today < level + row:
#                if jump > row:
#                    print("/", end="")
#                elif jump < -row:
#                    print("\\", end="")
#                else:
#                    print("_", end="")
#
#            elif abs(jump) > row and ((today < level <= tomorrow) or (tomorrow < level <= today)):
#                print("|", end="")
#            else:
#                print(" ", end="")
#        print()


#def plot(prices):
#    prices = [p["close"] for p in prices[-30:]]
#
#    low = min(prices)
#    high = max(prices)
#    diff = high - low
#    middle = (low + high) / 2
#    row = diff / 10
#
#    print("Highest Price:", high, "Lowest Price:", low)
#
#    rows = 10
#
#    # convert prices to row indices (0 = top)
#    pos = [int((high - p) / row) for p in prices]
#    pos = [min(rows - 1, max(0, r)) for r in pos]
#
#    for i in range(rows):
#
#        level = high - row * i
#
#        if i == 0:
#            print(f"{high:6.2f} |", end="")
#        elif i == 5:
#            print(f"{middle:6.2f} |", end="")
#        elif i == rows - 1:
#            print(f"{low:6.2f} |", end="")
#        else:
#            print("            |", end="")
#
#        for j in range(len(pos) - 1):
#            a = pos[j]
#            b = pos[j + 1]
#
#            if i == a == b:
#                print("_", end="")          # flat
#            elif i == a and b < a:
#                print("/", end="")          # up
#            elif i == a and b > a:
#                print("\\", end="")         # down
#            elif min(a, b) < i < max(a, b):
#                print("|", end="")          # vertical connector
#            else:
#                print(" ", end="")
#
#        print()

def plot(prices):
    prices = [p["close"] for p in prices[-30:]]

    low = min(prices)
    high = max(prices)
    rows = 10
    step = (high - low) / (rows - 1)

    # convert prices to row positions (0 = top)
    pos = [round((high - p) / step) for p in prices]

    for r in range(rows):

        if r == 0:
            print(f"{high:6.2f}  |", end="")
        elif r == rows // 2:
            mid = (high + low) / 2
            print(f"{mid:6.2f} |", end="")
        elif r == rows - 1:
            print(f"{low:6.2f} |", end="")
        else:
            print("            |", end="")

        for i in range(len(pos) - 1):
            a = pos[i]
            b = pos[i + 1]

            if r == a == b:
                c = "-"
            elif r == a and b < a:
                c = "/"
            elif r == a and b > a:
                c = "\\"
            elif a < r < b:
                c = "|"
            elif b < r < a:
                c = "|"
            else:
                c = " "

            print(c, end="")

        print()

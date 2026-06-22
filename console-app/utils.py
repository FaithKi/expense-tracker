def print_transactions(transactions: list):
    order = ["Name", "Type", "Category", "Amount", "Date"]
    width = [20, 15, 10, 9, 10]
    out = ""
    for i in range(len(order)):
        col = order[i]
        if len(col) < width[i]:
            col += (" "* (width[i] - len(col)))
        else:
            col = col[:width[i]]
        out += col
    print(f'\033[1m{out}\033[0m')
    for t in transactions:
        out = ""
        for i in range(len(order)):
            col = str(t[order[i].lower()])
            if len(col) < width[i]:
                col += (" "* (width[i] - len(col)))
            else:
                col = col[:width[i]]
            out += col
        print(out)
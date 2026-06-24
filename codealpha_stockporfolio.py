stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 350
}

total = 0

while True:
    stock = input("Enter stock name (or done): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        qty = int(input("Enter quantity: "))
        value = stocks[stock] * qty
        total += value
    else:
        print("Stock not found.")

print("Total Investment Value: $", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total}")

print("Saved to portfolio.txt")
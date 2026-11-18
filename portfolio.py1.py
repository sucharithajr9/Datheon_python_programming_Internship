import csv

# Sample stock prices
stock_prices = {
    "TCS": 4000,
    "INFY": 1800,
    "RELIANCE": 1400,
    "HDFC": 1700,
    "WIPRO": 550
}

portfolio = {}

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    ticker = input("\nEnter stock symbol (or done): ").strip().upper()

    if ticker == "DONE":
        break

    if ticker == "":
        print("Please enter a stock symbol.")
        continue

    buy_price = float(input("Enter buying price: "))
    quantity = int(input("Enter number of shares: "))

    if buy_price <= 0 or quantity <= 0:
        print("Price and quantity must be greater than zero.")
        continue

    if ticker in stock_prices:
        current_price = stock_prices[ticker]
    else:
        current_price = float(input("Enter current stock price: "))

    invested = buy_price * quantity
    market_value = current_price * quantity
    profit_loss = market_value - invested
    percentage = (profit_loss / invested) * 100

    portfolio[ticker] = [
        buy_price,
        quantity,
        current_price,
        invested,
        market_value,
        profit_loss,
        percentage
    ]

# Display portfolio summary
print("\n===== PORTFOLIO SUMMARY =====")

total_invested = 0
total_value = 0

for ticker, data in portfolio.items():
    print("\nStock:", ticker)
    print("Buying Price:", data[0])
    print("Quantity:", data[1])
    print("Current Price:", data[2])
    print("Invested:", data[3])
    print("Market Value:", data[4])
    print("Profit/Loss:", data[5])
    print("Gain/Loss Percentage:", round(data[6], 2), "%")

    total_invested += data[3]
    total_value += data[4]

print("\nTotal Investment:", total_invested)
print("Total Portfolio Value:", total_value)
print("Total Profit/Loss:", total_value - total_invested)

# Save portfolio details to CSV
with open("portfolio_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Ticker",
        "Buying Price",
        "Quantity",
        "Current Price",
        "Invested",
        "Market Value",
        "Profit/Loss",
        "Percentage"
    ])

    for ticker, data in portfolio.items():
        writer.writerow([ticker] + data)

print("\nCSV file generated successfully!")
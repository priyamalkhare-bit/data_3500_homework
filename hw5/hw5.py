import json

# Load stock prices from CSV file
def loadPrices(ticker):
    stock_prices = []

    file = open(f"{ticker}.csv", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        stock_price = round(float(line.strip()), 2)
        stock_prices.append(stock_price)

    return stock_prices

# Mean Reversion Strategy
def meanReversionStrategy(ticker,stock_prices):
    purchase_price = 0
    total_profit = 0
    first_buy_price = 0

    print("\n", ticker," Mean Reversion Strategy Output:")

    # start with 5 and end before 5
    for index in range(5, len(stock_prices)):
        moving_average = sum(stock_prices[index - 5:index]) / 5
        current_price = stock_prices[index]

        # Buy when current price is 2% below the 5-day average
        if purchase_price == 0 and current_price < moving_average * 0.98:
            purchase_price = current_price

            if first_buy_price  == 0:
                first_buy_price = current_price

            print(f"buying at: {round(current_price, 2)}")

        # Sell when current price is 2% above the 5-day average
        elif purchase_price !=0 and current_price > moving_average * 1.02:
            trade_profit = round(current_price - purchase_price, 2)
            total_profit += trade_profit

            print(f"selling at: {round(current_price, 2)}")
            print(f"trade profit: {round(trade_profit, 2)}")

            purchase_price = 0

    percent_return = 0

    if first_buy_price !=0:
        percent_return = (total_profit / first_buy_price) * 100

    total_profit = round(total_profit, 2)
    percent_return = round(percent_return, 2)

    print("-----------------------")
    print(f"Total profit: {total_profit}")
    print(f"Percent return: {percent_return}%")

    return total_profit, percent_return


# Simple Moving Average Strategy
def simpleMovingAverageStrategy(ticker,stock_prices):
    purchase_price = 0
    total_profit = 0
    first_buy_price = 0

    print("\n", ticker ," Simple Moving Average Strategy Output:")

    # start with 5 and end before 5
    for index in range(5, len(stock_prices)):
        moving_average = sum(stock_prices[index - 5:index]) / 5
        current_price = stock_prices[index]

        # Buy when current price is above the 5-day average
        if purchase_price ==0 and current_price > moving_average:
            purchase_price = current_price

            if first_buy_price==0:
                first_buy_price = current_price

            print(f"buying at: {round(current_price, 2)}")

        # Sell when current price is below the 5-day average
        elif purchase_price !=0 and current_price < moving_average:
            trade_profit = round(current_price - purchase_price, 2)
            total_profit += trade_profit

            print(f"selling at: {round(current_price, 2)}")
            print(f"trade profit: {round(trade_profit, 2)}")

            purchase_price = 0

    percent_return = 0

    if first_buy_price !=0:
        percent_return = (total_profit / first_buy_price) * 100

    total_profit = round(total_profit, 2)
    percent_return = round(percent_return, 2)

    print("-----------------------")
    print(f"Total profit: {total_profit}")
    print(f"Percent return: {percent_return}%")

    return total_profit, percent_return


# Save results to JSON file
def saveResults(results):
    with open("results.json", "w") as file:
        json.dump(results, file, indent=4)


tickers = [
    "AAPL",
    "GOOG",
    "ADBE",
    "MSFT",
    "AMZN",
    "TSLA",
    "CSCO",
    "CMCSA",
    "INTC",
    "NFLX"
]

results = {}

for ticker in tickers:
    stock_prices = loadPrices(ticker)

    results[f"{ticker}_prices"] = stock_prices

    mr_profit, mr_return = meanReversionStrategy(ticker,stock_prices)

    results[f"{ticker}_mr_profit"] = mr_profit
    results[f"{ticker}_mr_return"] = f"{mr_return}%"

    sma_profit, sma_return = simpleMovingAverageStrategy(ticker,stock_prices)

    results[f"{ticker}_sma_profit"] = sma_profit
    results[f"{ticker}_sma_return"] = f"{sma_return}%"

saveResults(results)

print("\nFinally I did it.Results are saved in results.json")

# read file
file = open("TSLA.txt")

# empty list
prices = []

# read one line at a time
lines = file.readlines()
for line in lines:
    # convert to float
    price = float(line)
    price = round(price, 2)  # to round the price to 2 decimals
    prices.append(price)

print("TSLA Mean Reversion Strategy Output: 2025 - 2026 Data")

buy_price = 0
first_buy_price = 0
total_profit = 0

# start with 6th postion so avg of previous 5 so moving avg can be calculated 
for index in range(5, len(prices)):
    print("-----------------------")
    current_price = prices[index]
    current_price = round(current_price, 2)

    # get previous 5 values
    previous_five_prices = prices[index - 5:index]

    Avg_price = sum(previous_five_prices) / 5
    Avg_price = round(Avg_price, 2)

    if current_price < Avg_price * 0.98:

        buy_price = current_price
        # buying for first time
        if first_buy_price == 0:
            first_buy_price = buy_price

        print(f"buying at:       {buy_price:.2f}")

    elif current_price > Avg_price * 1.02:

        sell_price = current_price

        trade_profit = sell_price - buy_price
        trade_profit = round(trade_profit, 2)

        total_profit = total_profit + trade_profit
        total_profit = round(total_profit, 2)

        print(f"selling at:      {sell_price:.2f}")
        print(f"trade profit:    {trade_profit:.2f}")

        buy_price = 0
    else:
        print("Do nothing")
        continue
        #do nothing
print("-----------------------")
print(f"Total profit:    {total_profit:.2f}")
print(f"First buy:       {first_buy_price:.2f}")

if first_buy_price != 0:
    final_profit_percentage = total_profit / first_buy_price * 100
    final_profit_percentage = round(final_profit_percentage, 2)

    print(f"% return:        {final_profit_percentage:.2f}%")
else:
    print("% return:        0.00%")
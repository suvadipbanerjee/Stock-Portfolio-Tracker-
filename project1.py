dic={"AAPL": 180, "TSLA": 250, "AMZN": 100, "GOOG": 1500, "MSFT": 300,
     "NFLX": 500, "FB": 350, "NVDA": 200, "INTC": 50, "AMD": 75}

Total_Investment = 0

input_stock = int(input("Enter How many stocks you want to buy: "))
for i in range(input_stock):
    input_stock_name = input("Enter the stock name: ").upper()
    input_stock_quantity = int(input("Enter the stock quantity: "))
    if input_stock_name in dic:
        Total_Investment += dic[input_stock_name] * input_stock_quantity
    else:
        print(f"{input_stock_name} is not in the stock list.")    

print(f"Total Investment: {Total_Investment}")
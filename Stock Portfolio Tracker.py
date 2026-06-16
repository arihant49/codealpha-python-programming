def stock_tracker():
    # Hardcoded dictionary defining stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 150,
        "MSFT": 420,
        "AMZN": 175
    }
    
    portfolio = {}
    
    print("--- CodeAlpha Stock Portfolio Tracker ---")
    print("Available Stocks to add:", ", ".join(stock_prices.keys()))
    print("Type 'done' when you are finished adding stocks.\n")
    
    while True:
        stock_name = input("Enter Stock Name (e.g., AAPL): ").upper().strip()
        
        if stock_name == 'DONE':
            break
            
        if stock_name not in stock_prices:
            print("Stock symbol not found in our system. Please try a valid symbol.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")
            continue
            
        # Update portfolio (adds up if the user enters the same stock multiple times)
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name} to your tracking list.\n")

    # Calculate and display total investment summary
    print("\n" + "="*35)
    print("        PORTFOLIO SUMMARY        ")
    print("="*35)
    
    total_investment = 0.0
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        stock_value = qty * price
        total_investment += stock_value
        print(f"{stock}: {qty} shares @ ${price} each = ${stock_value:,.2f}")
        
    print("-" * 35)
    print(f"Total Portfolio Value: ${total_investment:,.2f}")
    print("="*35)

if __name__ == "__main__":
    stock_tracker()
from stock import Stock
from trade_book import Tradebook
import csv
import decimal
 
 
 #Global list so as accessible to other methods
trades = []
tradebook = Tradebook()
def main():
    #Stock instances
    stock1 = Stock("id1", "CHX", "FB", 100.00, 120, "sell")
    print(stock1)
    stock2 = Stock("id2", "NASDAQ", "AAPL", 150.50, 75, "buy")
    print(stock2)
    stock3 = Stock("id3", "CHX", "ORCL", 70.22, 160, "sell")
    print(stock3)
    stock4 = Stock("id4", "NYSE", "F", 50.34, 200, "buy")
    print(stock4)
    stock5 = Stock("id5", "NASDAQ", "AAPL", 155.99, 65, "buy")
    print(stock5)
    stock6 = Stock("id6", "NASDAQ", "F", 55.12, 200, "buy")
    print(stock6)
    stock7 = Stock("id7", "NYSE", "FB", 100.34, 120, "sell")
    print(stock7)
    stock8 = Stock("id8", "CHX", "AAPL", 150.44, 75, "buy")
    print(stock8)
    stock9 = Stock("id9", "NYSE", "AAPL", 150.73, 80, "sell")
    print(stock9)
    stock10 = Stock("id10", "CHX", "ORCL", 75.89, 170, "sell")
    print(stock10)    


    # Add the trades to the Tradebook
    tradebook.add(stock1)
    tradebook.add(stock2)
    tradebook.add(stock3)
    tradebook.add(stock4)
    tradebook.add(stock5)
    tradebook.add(stock6)
    tradebook.add(stock7)
    tradebook.add(stock8)
    tradebook.add(stock9)
    tradebook.add(stock10)
    #Read and process the trades from csv vile
    read_trades_from_csv()

    #Print out trades
    #show_trades(trades)
   
    #Calculate value of trades
    total_value = total_value_of_trades(trades)
    print(total_value)

    #Calculate value of trades based on symbol
    symbolTradeValue = total_value_by_sym(trades)
    print(symbolTradeValue)

    #Calculate value of trades based on exchange
    exchangeTradeValue = total_value_by_exchange(trades)
    print(exchangeTradeValue )
    
    print('-- Printing from tradebook --')
    # Generate and print the statistics
    tradebook.print_reference_trades_statistics()
    tradebook.print_small_trades_statistics()
    tradebook.print_large_trades_statistics()

def read_trades_from_csv():
    #prompt user for file path
    file_path = input ("Please enter the path to the transaction file")

    with open (file_path, 'r', newline = '') as csvfile:
        #split line by ;
        reader = csv.reader(csvfile, delimiter = ';')
        for line_no , line in enumerate(reader, start =1):
            time,exchange,symbol,quantity,price,side = line
            id = f"id{line_no}"
            price = decimal.Decimal(price)
            stock = Stock(id,exchange, symbol, price, int(quantity), side)
            trades.append(stock)
            tradebook.add(stock)

def show_trades(trades):
    for trade in trades:
        print(trade)
    
       
def total_value_of_trades(trades):
        total_value = 0
        for trade in trades:
            total_value += trade.calculate_value()
        return f"\nThe total value of all trades is : ${total_value}"

def total_value_by_sym(trades):
    symbol = input ("Enter the Symbol you want to calculate total value for")
    trades_filtered = [trade for trade in trades if trade.symbol == symbol]
    total_buy = 0
    total_sell = 0

    for trade in trades_filtered:
        if trade.side == 'buy':
             total_buy += trade.calculate_value()

        elif trade.side == 'sell':
           total_sell += trade.calculate_value()
    return f"The total value of all {symbol} bought trades is: $ {total_buy}\n" \
           f"The total value of all {symbol} sold trades is: $ {total_sell}"


def total_value_by_exchange(trades):
    exchange = input("Enter the Exchange you want to calculate total value for")
    trades_filtered = [trade for trade in trades if trade.exchange == exchange]

    total_buy= 0
    total_sell = 0

    for trade in trades_filtered:
        if trade.side == 'buy':
            total_buy += trade.calculate_value()
        elif trade.side == 'sell':
            total_sell += trade.calculate_value()
    return f"The total value of all {exchange} bought trades is: $ {total_buy}\n" \
           f"The total value of all {exchange} sold trades is: $ {total_sell}"

        

 


if __name__ == '__main__':
    main()



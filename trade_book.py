import stock
class Tradebook ():
    def __init__(self):
        self.first_trade = None
        self.reference_trades = []
        self.small_trades = []
        self.large_trades = []

    def add(self, new_trade):
        if self.first_trade is None:
            self.first_trade = new_trade
            self.reference_trades.append(self.first_trade)
        if new_trade > self.first_trade:
            self.large_trades.append(new_trade)
        elif new_trade < self.first_trade:
            self.small_trades.append(new_trade)
        else:
            self.reference_trades.append(new_trade)

    def print_reference_trades_statistics(self):
        count = len(self.reference_trades)
        total_value = 0
        for trade in self.reference_trades:
            total_value+=trade.calculate_value()
        total_value
        average_value = total_value/count if count else 0
        print( f"\nThe summary of reference trades statistics\n"\
            f"There are {count} items in list with an average value of {average_value}\n")


    # small_trades_statistics()
    def print_small_trades_statistics(self):
        count = len(self.small_trades)
        total_value = sum(trade.calculate_value() for trade in self.small_trades)
        average_value = total_value/count if count else 0
        print( f"\nThe summary of small trades statistics\n"\
            f"There are {count} items in list with an average value of {average_value}")

    # large_trades_statistics()
    def print_large_trades_statistics(self):
        count = len(self.large_trades)
        total_value = sum(trade.calculate_value() for trade in self.large_trades)
        average_value = total_value/count if count else 0
        print( f"\nThe summary of large trades statistics\n"\
            f"There are {count} items in list with an average value of {average_value}")
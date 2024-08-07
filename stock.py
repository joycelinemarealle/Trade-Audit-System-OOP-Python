
from trade import Trade
import decimal
class Stock(Trade):
    def __init__(self,id,exchange,symbol, price, quantity, side):
        super().__init__(id, exchange, symbol, decimal.Decimal(price), quantity, side)
    
    #overiding abstract method
    def calculate_value(self):
        return self.price * self.quantity
    
    #operator overloading
    def __lt__(self, other):
        return self.calculate_value() < other.calculate_value()

    def __eq__(self,other):
        return self.calculate_value() == other.calculate_value()

    def __gt__(self, other):
        return self.calculate_value() > other.calculate_value()

    def __str__(self):
        return (f"Stock (ID: {self.id},EXCHANGE: {self.exchange},"
        f"SYMBOL: {self.symbol}, PRICE: {self.price},"
        f"QUANTITY: {self.quantity}, SIDE: {self.side})")
    
    
    #Additional methods specific to stock trade
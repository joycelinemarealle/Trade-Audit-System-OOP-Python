"""The base class for all trades"""
from abc import ABCMeta, abstractmethod
import decimal

class Trade(metaclass=ABCMeta):
    def __init__(self, id, exchange, symbol, price, quantity, side):
        if price <= 0.0 :
            raise ValueError("${price}: Price cannot be negative")
        if quantity <= 0:
           raise ValueError ("{quantity}: Quantity cannot be negative")
        self.id = id
        self.exchange = exchange
        self.symbol = symbol
        self.price = decimal.Decimal(price)
        self.quantity = quantity
        self.side = side

    @property
    def quantity(self):
        return self._quantity
    
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def exchange(self):
        return self._exchange

    @quantity.setter
    def quantity(self, value):
          self._quantity = value
    
    @symbol.setter
    def symbol(self, value):
          self._symbol = value
    
    @exchange.setter
    def exchange(self, value):
          self._exchange = value
    
    @quantity.deleter
    def quantity(self):
        del self._quantity


    @abstractmethod
    #must be implemented by subclasses
    def calculate_value(self):
       pass
    
    def __str__(self):
        return (f"TRADE (ID: {self.id}, EXCHANGE:{self.exchange},"
        f"SYMBOL : {self.symbol}, PRICE : {self.price},"
        f"QUANTITY : {self.quantity}, SIDE :{self.side})")
    

    """
    @classmethod(cls)
    def create_stock(id, exchange, symbol, price, quantity, side): # Factory method
        if price <= 0:
            raise ValueError('${self.price}: Price cannot be 0 or a negative number')
        if quantity <= 0:
            raise ValueError('${self.quantity}: Quantity cannot be 0 or a negative number')
        if side.upper() != "BUY" or side.upper() != "SELL":
            raise ValueError('${self.side}: Side can either be SELL or BUY')
        return cls(id, exchange, symbol, price, quantity, side)
 """
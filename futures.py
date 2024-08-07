from trade import Trade

class Futures(Trade):
    def __init__(self, id, exchange, symbol, price, quantity, side,expiry_date):
        super().__init__(id, exchange, symbol,price,quantity,side)
        self.expiry_date = expiry_date

        ##specific methoda for Futures
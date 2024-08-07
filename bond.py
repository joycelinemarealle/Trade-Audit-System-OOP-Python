from trade import Trade

class Bond(Trade):
    def __init__(self, id, exchange, symbol, price, quantity, side, maturity_date):
        super().__init__(id, exchange, symbol, price, quantity, side)
        self.maturity_date = maturity_date


        #specific methods for bond
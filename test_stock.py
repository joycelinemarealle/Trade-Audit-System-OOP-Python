import unittest
import stock

class Test_Stock(unittest.TestCase):
    def setUp(self):
        #an instance of stock each time method is run
        self.stock = stock.Stock("id1", "NYSE", "TSL", 208.00, 10, "buy") 

    def test_create_stock(self):
        #Test if stock instance is created with correct attributes
        self.assertEqual(self.stock.id, "id1" )
        self.assertEqual(self.stock.exchange, "NYSE")
        self.assertEqual(self.stock.symbol, "TSL")
        self.assertEqual(self.stock.price , 208.00)
        self.assertEqual(self.stock.quantity, 10)
        self.assertEqual(self.stock.side, "buy")

    def test_calculate_value(self):
        expected_value = self.stock.price* self.stock.quantity
        self.assertEqual(self.stock.calculate_value(), expected_value)
    
    def test_stock_quantity(self):
        self.stock.quantity = 20
        self.assertEqual(self.stock.quantity, 20)
    
    def test_negative_price_error(self):
       #returns true when error raised
       with self.assertRaises(ValueError):
           self.stock2 = stock.Stock ("id1", "NYSE", "TSL", -208.00, 10, "buy")

    def test_negative_quantity_error(self):
       #returns true when error raised
       with self.assertRaises(ValueError):
           self.stock2 = stock.Stock ("id1", "NYSE", "TSL", 208.00, -10, "buy")



if __name__ == '__main__':
    unittest.main()
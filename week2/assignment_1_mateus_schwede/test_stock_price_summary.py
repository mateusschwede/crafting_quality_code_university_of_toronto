import a1, unittest

class TestStockPriceSummary(unittest.TestCase):
    #Test class for a1.stock_price_summary

    def test_stock_price_summary_no_loss_no_gain(self):
        #Test for no loss no gain for 1 info only
        expct = (0, 0)
        act = a1.stock_price_summary([0])
        self.assertEqual(expct, act)

    def test_stock_price_summary_no_info_at_all(self):
        #Test for no given no information that is empty list given
        expct = (0, 0)
        act = a1.stock_price_summary([])
        self.assertEqual(expct, act)

    def test_stock_price_summary_integers_gains(self):
        #Test stock_price_summary for integer list of gains only
        expct = (6, 0)
        act = a1.stock_price_summary([1,2,3])
        self.assertEqual(expct, act)

    def test_stock_price_summary_integers_losses(self):
        #Test stock_price_summary for integer list of losses only
        expct = (0, -6)
        act = a1.stock_price_summary([-1,-2,-3])
        self.assertEqual(expct, act)

    def test_stock_price_summary_integers(self):
        #Test stock_price_summary for gains and losses in integer list
        expct = (11.0, -7.0)
        act = a1.stock_price_summary([3, 6,-3, 2,-4])
        self.assertEqual(expct, act)

    def test_stock_price_summary_losses(self):
        #Test stock_price_summary for losses only
        expct = (0.0, -0.75)
        act = a1.stock_price_summary([-0.3,-0.4,-0.05])
        self.assertEqual(expct, act)

    def test_stock_price_summary_gains(self):
        #Test stock_price_summary for gains only
        expct = (1.0, 0.0)
        act = a1.stock_price_summary([0.5,0.4,0.005,0.095])
        self.assertEqual(expct, act)
        
    def test_stock_price_summary_losses_gains(self):
        #Test stock_price_summary for gains and losses
        expct = (0.14, -0.17)
        act = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        self.assertEqual(expct, act)

if __name__ == '__main__':
    unittest.main(exit=False)
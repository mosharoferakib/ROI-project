import unittest
from rental_property import RentalProperty

class TestRentalProperty(unittest.TestCase):
    def test_calculate_roi(self):
        # Test with a rental property that generates profit
        property1 = RentalProperty(purchase_price=500000, rental_income=2000, operating_expenses=1000, holding_period_years=5, selling_price=600000)
        roi1 = property1.calculate_roi()
        self.assertAlmostEqual(roi1, 15.38, places=2)

        # Test with a rental property that generates a loss
        property2 = RentalProperty(purchase_price=500000, rental_income=1500, operating_expenses=2000, holding_period_years=5, selling_price=450000)
        roi2 = property2.calculate_roi()
        self.assertAlmostEqual(roi2, -11.54, places=2)

if __name__ == '__main__':
    unittest.main()

class RentalProperty:
    def __init__(self, purchase_price, rental_income, operating_expenses, holding_period_years, selling_price):
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.operating_expenses = operating_expenses
        self.holding_period_years = holding_period_years
        self.selling_price = selling_price
    
    def calculate_roi(self):
        total_income = self.rental_income * self.holding_period_years
        total_expenses = self.operating_expenses * self.holding_period_years
        net_profit = (self.selling_price - self.purchase_price) - total_expenses
        total_investment = self.purchase_price + total_expenses
        roi = (net_profit / total_investment) * 100
        return roi



property1 = RentalProperty(purchase_price=500000, rental_income=2000, operating_expenses=1000, holding_period_years=5, selling_price=600000)

# Calculate the ROI
roi = property1.calculate_roi()
print(f"The ROI for this rental property is {roi:.2f}%")

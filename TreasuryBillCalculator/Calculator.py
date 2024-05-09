ratesDownload = __import__('ratesDownload').ratesDownload


class Calculator:
    def __init__(self, face_value, duration):
        self.rates = ratesDownload()
        self.face_value = face_value
        self.duration = duration
        self.maturityDays = int(self.duration)
        self.durationRates = self.getRates()
        self.discount_price = float(self.durationRates['discount']) / 100
        self.interest_rate = float(self.durationRates['interest']) /100
        self.days = self.durationRates['duration']
        self.price = self.calculate_purchase_price()


    def getRates(self):
        self.rates_data = self.rates[self.duration]
        return self.rates_data

    def calculate_purchase_price(self):
        self.purchase_price = int(self.face_value) * (1 - (self.discount_price * self.maturityDays / 365))
        return round(self.purchase_price, 2)

    def effective_annual_yield(self):
        self.annual_yeild = ((self.face_value / self.purchase_price) ** (365 / self.maturityDays)) - 1
        return round(self.annual_yeild, 4)

    def interest_earned(self):
        self.interest = self.face_value - self.purchase_price
        return round(self.interest, 2)

    def final_amount_earned(self):
        return self.face_value + self.interest_earned()





cal = Calculator(1000, '91')
duration_rates = cal.final_amount_earned()
print(duration_rates)
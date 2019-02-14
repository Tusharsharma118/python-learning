class CurrencyException(BaseException):
    def __init__(self, message):
        super().__init__(message)


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr(self.currency,self.amount)

    def __add__(self, other):
        if type(self) != type(other):
            raise CurrencyException(' Not a valid currency!!!')
        if self.currency == other.currency:
            currency = self.currency
            final_amount = self.amount + other.amount
        else:
            raise CurrencyException('Currency Types do not Match!')
        return Currency(currency, final_amount)

class FakeCurrency: pass


dollar = Currency('USD', 50)

rupee = Currency('INR', 60)

ressult = dollar + FakeCurrency()

print(f""" Final Currency: {ressult.currency} \n Final Amount: {ressult.amount}""")

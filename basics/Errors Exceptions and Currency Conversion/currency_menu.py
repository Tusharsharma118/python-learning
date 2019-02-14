class CurrencyException(BaseException):
    def __init__(self, message):
        super().__init__(message)


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr((self.currency,self.amount))

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


class CurrencyConverter():
    def __init__(self, currency_from : str, currency_to : str, conversion_rate):
        self.convert_to = currency_to;
        self.convert_from = currency_from;
        self.conversion_rate = conversion_rate

    def convert_currency(self, amount, currency_from: str, currency_to : str):
        # if type(currency_from) != type(currency_to):
        #    raise CurrencyException('Fake Curency!')
        if self.convert_from != currency_from or self.convert_to != currency_to:
            raise CurrencyException('Icompatible Currency Conversion!')
        else:
            return Currency(self.convert_to,(amount * self.conversion_rate))


dollar: Currency = Currency('USD', 50)

rupee : Currency = Currency('INR', 60)

# result = dollar + FakeCurrency()

usd_to_inr = CurrencyConverter('USD','INR', 71)

# print(f""" Final Currency: {result.currency} \n Final Amount: {ressult.amount}""")

curr = usd_to_inr.convert_currency(dollar.amount,dollar.currency,rupee.currency)

print(f"""  Converting dollars { dollar } to inr : {curr}   """)
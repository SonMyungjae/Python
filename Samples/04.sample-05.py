# 환율
from currency_converter import CurrencyConverter

# cc = CurrencyConverter()
cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')

# print(cc.currencies)
print(cc.convert(1, 'USD', 'KRW'))
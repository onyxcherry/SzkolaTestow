class Wallet:
  def __init__(self, stock):
    self.base_currency = stock.get_base_currency
    self.quantity = stock.get_quantity

  def value(self, currency: str, rate_provider: object) -> float:
    rate = rate_provider.rate(self.base_currency, currency)
    value = round(rate * self.quantity, 2)
    return value

class Wallet:
  def __init__(self, stock):
    self.base_currency = stock.get_base_currency

  def value(self, currency, rate_provider):
    value = rate_provider.rate(self.base_currency, currency)
    return value
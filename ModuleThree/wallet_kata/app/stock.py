class Stock:
  def __init__(self, quantity, currency):
    self._quantity = quantity
    self._currency = currency

  @property
  def get_base_currency(self):
    return self._currency

  @property
  def get_quantity(self):
    return self._quantity

class Stock:
  def __init__(self, quantity: int, currency: str):
    self._quantity = quantity
    self._currency = currency

  @property
  def get_base_currency(self) -> str:
    return self._currency

  @property
  def get_quantity(self) -> int:
    return self._quantity

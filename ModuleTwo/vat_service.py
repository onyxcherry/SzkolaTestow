class VatService:
  def __init__(self) -> None:
    self.vat_value = 0.23

  def get_gross_price_for_default_vat(self, product: object) -> float:
    return self.get_gross_price(product.net_price, self.vat_value)

  def get_gross_price(self, net_price: float, vat_value: float) -> float:
    if not 0 < vat_value < 1:
      raise ValueError('VAT value must be in range 0-1')

    gross_price = net_price * (1 + vat_value)
    return round(gross_price, 2)


class Product:
  def __init__(self, product_id: int, net_price: float) -> None:
    self.id = product_id
    self.net_price = net_price

  def __repr__(self) -> str:
    return f'<class Product id {self.id}>'

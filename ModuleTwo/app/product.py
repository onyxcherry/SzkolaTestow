class Product:
  def __init__(self, product_id: int, net_price: float) -> None:
    self.id = product_id
    self.net_price = net_price

  def __repr__(self) -> str:
    return f'<class Product id {self.id}>'

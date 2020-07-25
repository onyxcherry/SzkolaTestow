class Product:
  def __init__(self, product_id: int, net_price: float,
               product_type: str) -> None:
    self.id = product_id
    self.net_price = net_price
    self.type = product_type

  def get_net_price(self) -> float:
    return self.net_price

  def __repr__(self) -> str:
    return f'<class Product id {self.id}>'

import logging


class Product:
  def __init__(self, product_id: int, net_price: float,
               product_type: str) -> None:
    self.id = product_id
    self.net_price = net_price
    self.type = product_type
    logging.debug(
      f'Created instance of Product with {product_id} as id, '
      f'{net_price} as net price, {product_type} as type')

  def get_net_price(self) -> float:
    logging.debug('Called get_net_price method')
    return self.net_price

  def get_product_type(self) -> str:
    logging.debug('Called get_product_type method')
    return self.type

  def __repr__(self) -> str:
    return f'<class Product id {self.id}>'

import logging

from .vat_provider import VatProvider


class VatService:
  """
  Calculate Gross price for given product's price
  """

  def __init__(self) -> None:
    self.vat_provider = VatProvider()
    logging.debug('Created instance of VatService')

  def get_gross_price_for_default_vat(self, product) -> float:
    net_price = product.get_net_price()
    logging.debug(f'Called get_gross_price_for_default_vat method with '
                  f'{product} which net price is {net_price}')
    return self.calculate_gross_price(net_price,
                                      self.vat_provider.get_default_vat())

  def get_gross_price(self, net_price: float, product_type: str) -> float:
    logging.debug(f'Called get_gross_price method with {net_price} as net price'
                  f' and {product_type} as product type')
    vat_value = self.vat_provider.get_vat_for_given_type(product_type)
    logging.debug(f'Called VatProvider\'s get_vat_for_given_type method '
                  f'and returned {vat_value}')
    return self.calculate_gross_price(net_price, vat_value)

  @staticmethod
  def calculate_gross_price(net_price: float, vat_value: float):
    if not 0 < vat_value < 1:
      logging.warning('VAT value out of valid range')
      raise ValueError('VAT value must be in range 0-1')
    gross_price = net_price * (1 + vat_value)
    logging.debug('Calculated gross price')
    # Note that price should be rounded to a two decimal places
    return round(gross_price, 2)

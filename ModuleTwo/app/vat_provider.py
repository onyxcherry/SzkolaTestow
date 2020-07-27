import logging
from time import sleep


class VatProvider:
  """
  External, expensive and time-consuming API
  """

  def __init__(self):
    logging.debug('Created instance of VatProvider')

  @staticmethod
  def get_default_vat() -> float:
    logging.debug('Called get_default_vat method')
    sleep(7)
    return 0.23

  @staticmethod
  def get_vat_for_given_type(product_type: str) -> float:
    logging.debug(f'Called get_vat_for_given_type with {product_type} as type')
    sleep(9)
    random_value = 0.05
    return random_value

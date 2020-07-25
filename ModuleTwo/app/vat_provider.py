from time import sleep


class VatProvider:
  """
  External, expensive and time-consuming API
  """

  @staticmethod
  def get_default_vat() -> float:
    sleep(7)
    return 0.23

  @staticmethod
  def get_vat_for_given_type(type: str) -> float:
    sleep(9)
    random_value = 0.05
    return random_value

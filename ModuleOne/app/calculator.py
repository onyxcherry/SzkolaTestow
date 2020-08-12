from typing import Union


class StringCalculator:
  """
  Add given numbers as text line, separated by a comma.
  Spaces are allowed. Floating point are supported.
  """

  def add(self, user_input: str) -> Union[int, float]:
    if self.check_if_input_is_zero(user_input):
      return 0
    string_numbers = user_input.split(',')
    result = 0
    for string_number in string_numbers:
      string_number = string_number.strip()
      if string_number.isdigit():
        result += int(string_number)
      elif self.try_convert_to_float(string_number):
        number = self.try_convert_to_float(string_number)
        result += float(number)
      else:
        raise Exception('Invalid format')
    return result

  @staticmethod
  def check_if_input_is_zero(user_input: str) -> bool:
    if user_input is None or user_input.strip() == '':
      return True

  @staticmethod
  def try_convert_to_float(string_number: str) -> float:
    try:
      return float(string_number)
    except ValueError:
      return 0

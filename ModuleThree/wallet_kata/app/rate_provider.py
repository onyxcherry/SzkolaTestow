import requests
import json


class RateProvider:
  @staticmethod
  def rate(stock_type: str, currency: str) -> float:
    url = f'https://api.exchangeratesapi.io/latest?base={stock_type}' \
          f'&symbols={currency}'
    response = requests.get(url)
    jsoned_response_content = json.loads(response.content)
    try:
      rate = jsoned_response_content['rates'][currency]
    except KeyError as key_error:
      print(f'Unsupported currency in {key_error}')
      return None
    return rate

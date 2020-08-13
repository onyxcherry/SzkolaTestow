import json
import sys
from typing import Union

import requests


class RateProvider:

  def rate(self, stock_type: str, currency: str) -> float:
    url = f'https://api.exchangeratesapi.io/latest?base={stock_type}' \
          f'&symbols={currency}'
    rate = self.get_latest_rate(url, currency)
    return rate

  def get_latest_rate(self, url: str, currency: str) -> float:
    response_content = self.get_response_content(url)
    json_response_content = self.get_response_content_as_json(response_content)
    rate = self.get_rate_from_response(json_response_content, currency)
    return rate

  @staticmethod
  def get_response_content(url: str) -> bytes:
    return requests.get(url).content

  @staticmethod
  def get_response_content_as_json(response_content: bytes) -> dict:
    return json.loads(response_content)

  @staticmethod
  def get_rate_from_response(json_response_content: dict,
                             currency: str) -> Union[float, None]:
    try:
      rate = json_response_content['rates'][currency]
    except KeyError as key_error:
      print(f'Unsupported currency in {key_error}', file=sys.stderr)
      return None
    return rate

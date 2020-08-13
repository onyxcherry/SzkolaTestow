from unittest.mock import patch

from pytest import mark


@patch('app.rate_provider.RateProvider.get_response_content',
       return_value=b'{"error":"Base \'petroleum\' is not supported."}')
def test_not_available_currency_in_external_api(mocked_response, rate_provider):
  rate = rate_provider.rate('petroleum', 'USD')
  assert rate is None


@mark.skip(reason='Do not overuse external API')
def test_rate_provider_rate_call_external_api(rate_provider):
  rate = rate_provider.rate('USD', 'EUR')
  assert isinstance(rate, float)


@patch('app.rate_provider.RateProvider.rate', return_value=0.85)
def test_rate_provider_calculate_response_type(mocked_rate, rate_provider):
  rate = rate_provider.rate('USD', 'EUR')
  assert isinstance(rate, float)
  mocked_rate.assert_called()

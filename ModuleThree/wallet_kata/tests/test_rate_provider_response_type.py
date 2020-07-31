from unittest.mock import patch

from app import RateProvider


@patch('app.rate_provider.RateProvider.rate', return_value=0.85)
def test_rate_provider_calculate_response_type(mocked_rate):
  rate_provider = RateProvider()
  rate = rate_provider.rate('USD', 'EUR')
  assert isinstance(rate, float)
  mocked_rate.assert_called()
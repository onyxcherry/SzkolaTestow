from unittest.mock import patch

from app import Stock, Wallet

return_value = 0.85157


@patch('app.rate_provider.RateProvider.rate', return_value=return_value)
def test_wallet_value(mocked_rate, rate_provider):
  value = Wallet(Stock(7, 'USD')).value('EUR', rate_provider)
  assert isinstance(value, float)
  assert value == 5.96
  mocked_rate.assert_called()

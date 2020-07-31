from app import RateProvider


def test_not_available_currency_external_api():
  rate_provider = RateProvider()
  rate = rate_provider.rate('petroleum', 'USD')
  assert rate is None

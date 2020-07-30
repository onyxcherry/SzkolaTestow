from app import RateProvider, Stock, Wallet


def test_passing_object_to_wallet():
  rate_provider = RateProvider()
  wallet = Wallet(Stock(5, 'USD')).value('EUR', rate_provider)


def test_rate_provider_calculate():
  rate_provider = RateProvider()
  rate_provider.rate('USD', 'EUR')

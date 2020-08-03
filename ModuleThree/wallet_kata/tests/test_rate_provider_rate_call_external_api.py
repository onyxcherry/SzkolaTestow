from pytest import mark

from app import RateProvider


@mark.skip(reason='Do not overuse external API')
def test_rate_provider_rate_call_external_api():
  rate_provider = RateProvider()
  rate = rate_provider.rate('USD', 'EUR')
  assert isinstance(rate, float)

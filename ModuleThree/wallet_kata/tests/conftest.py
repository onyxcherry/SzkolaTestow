import pytest

from app import RateProvider


@pytest.fixture(scope='session')
def rate_provider():
  rate_provider = RateProvider()
  return rate_provider

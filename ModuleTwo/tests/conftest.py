import pytest

from app import VatService


@pytest.fixture(scope='session')
def vat_service():
  vat_service = VatService()
  return vat_service

import pytest

from app import VatService


@pytest.fixture(scope='session')
def vat_service():
  valid_vat_service = VatService()
  return valid_vat_service

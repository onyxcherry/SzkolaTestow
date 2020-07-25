import pytest
from pytest_mock import session_mocker

from app import VatService


@pytest.fixture(scope='session')
def vat_service():
  vat_service = VatService()
  return vat_service


@pytest.fixture(scope='session')
def setup_mocker():
  return session_mocker

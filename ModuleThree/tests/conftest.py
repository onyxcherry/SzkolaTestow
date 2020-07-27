import pytest

from app import Bowling


@pytest.fixture(scope='session')
def bowling():
  bowling = Bowling()
  return bowling

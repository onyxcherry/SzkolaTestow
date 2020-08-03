import pytest

from app import Bowling


@pytest.fixture(scope='function')
def bowling():
  bowling = Bowling()
  return bowling

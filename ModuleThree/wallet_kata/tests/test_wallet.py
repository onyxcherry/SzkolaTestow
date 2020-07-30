from app import Stock
from app import Wallet


def test_passing_object_to_wallet():
  wallet = Wallet(Stock(5, 'USD'))

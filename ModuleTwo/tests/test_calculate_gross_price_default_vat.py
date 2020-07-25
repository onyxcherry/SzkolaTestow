from uuid import uuid1
from app.vat_service import Product

product = Product(int(uuid1()), 6.74)


def test_calculating_gross_price_for_default_vat(vat_service):
  # Default VAT value is 23% so when rounded 6.74 * 1,23, we'll get 8.29
  assert vat_service.get_gross_price_for_default_vat(product) == 8.29

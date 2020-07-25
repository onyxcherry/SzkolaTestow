from uuid import uuid1

from assertpy import assert_that

from app import Product

product = Product(int(uuid1()), 6.74, 'sweatshirt')


def test_calculating_gross_price_for_default_vat(vat_service, mocker):
  mocker.patch('app.vat_provider.VatProvider.get_default_vat',
               return_value=0.23)
  result = vat_service.get_gross_price_for_default_vat(product)
  # Default VAT value is 23% so when rounded 6.74 * 1,23, we'll get 8.29
  assert_that(result).is_equal_to(8.29)
  assert_that(result).is_not_equal_to(8.28)

from unittest import mock
from uuid import uuid1

from assertpy import assert_that

from app import Product

mocked_default_vat = 'app.vat_provider.VatProvider.get_default_vat'


@mock.patch(mocked_default_vat, return_value=0.23, autospec=True)
def test_calculating_gross_price_for_default_vat(mocked_vat, vat_service):
  product = Product(int(uuid1()), 6.74, 'sweatshirt')
  result = vat_service.get_gross_price_for_default_vat(product)
  # Default VAT value is 23% so when rounded 6.74 * 1,23, we'll get 8.29
  assert_that(result).is_equal_to(8.29)
  assert_that(result).is_not_equal_to(8.28)
  mocked_vat.assert_called_with()


mocked_determined_vat = 'app.vat_provider.VatProvider.get_vat_for_given_type'


@mock.patch(mocked_determined_vat, return_value=0.05, autospec=True)
def test_calculating_gross_price_for_determined_vat(mocked_vat, vat_service):
  product_type = 'boots'
  result = vat_service.get_gross_price(13.70, product_type)
  assert_that(result).is_equal_to(14.38)
  assert_that(result).is_not_equal_to(14.39)
  mocked_vat.assert_called_with(product_type)


def test_calculate_gross_price_for_given_valid_vat(vat_service):
  result = vat_service.calculate_gross_price(29.99, 0.08)
  assert_that(result).is_equal_to(32.39)
  assert_that(result).is_not_equal_to(32.40)

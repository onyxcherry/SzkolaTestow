import logging
from unittest import mock
from uuid import uuid1

from assertpy import assert_that

from app import Product

product = Product(int(uuid1()), 6.74, 'sweatshirt')

mocked_method_location = 'app.vat_provider.VatProvider.get_default_vat'


@mock.patch(mocked_method_location, return_value=0.23, autospec=True)
def test_calculating_gross_price_for_default_vat(mocked_vat, vat_service):
  result = vat_service.get_gross_price_for_default_vat(product)
  logging.debug('Called get_gross_price_for_default_vat method')
  # Default VAT value is 23% so when rounded 6.74 * 1,23, we'll get 8.29
  assert_that(result).is_equal_to(8.29)
  logging.info('Returned correct VAT value')
  assert_that(result).is_not_equal_to(8.28)
  logging.info('Compared to incorrect value')
  mocked_vat.assert_called_with()
  logging.info('Checked if mocked method called without arguments')

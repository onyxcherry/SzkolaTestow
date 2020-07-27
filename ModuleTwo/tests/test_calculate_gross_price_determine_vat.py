import logging
from unittest import mock

from assertpy import assert_that

mocked_method_location = 'app.vat_provider.VatProvider.get_vat_for_given_type'


@mock.patch(mocked_method_location, return_value=0.05, autospec=True)
def test_calculating_gross_price_for_determined_vat(mocked_vat, vat_service):
  product_type = 'boots'
  result = vat_service.get_gross_price(13.70, product_type)
  logging.debug('Got gross price determined based on item category type')
  assert_that(result).is_equal_to(14.38)
  logging.info('Returned correct gross price')
  assert_that(result).is_not_equal_to(14.39)
  logging.info('Compared to incorrect value')
  mocked_vat.assert_called_with(product_type)
  logging.info(f'Mocked method called with "{product_type}" as an argument')

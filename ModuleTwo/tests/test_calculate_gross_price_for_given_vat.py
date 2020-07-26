import logging

from assertpy import assert_that

from app import VatService

vat_service = VatService()


def test_calculate_gross_price_for_given_valid_vat():
  result = vat_service.calculate_gross_price(29.99, 0.08)
  logging.debug('Got gross price')
  assert_that(result).is_equal_to(32.39)
  logging.info('Correct gross price')
  assert_that(result).is_not_equal_to(32.40)
  logging.info('Compared to incorrect value')

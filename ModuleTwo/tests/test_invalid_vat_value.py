import logging

import pytest
from assertpy import assert_that


def test_throw_exception_when_invalid_vat_value(vat_service):
  with pytest.raises(ValueError) as value_error:
    logging.debug('Pass invalid VAT value and expect exception')
    vat_service.calculate_gross_price(18.59, 2.56)
    logging.info('Handled expected exception')
  assert_that(str(value_error.value)).contains('range', '0', '1')
  logging.info('Exception message contains correct range values')

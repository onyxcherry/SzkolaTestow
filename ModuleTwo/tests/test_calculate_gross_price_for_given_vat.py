from assertpy import assert_that

from app import VatService

vat_service = VatService()


def test_calculate_gross_price_for_given_valid_vat():
  result = vat_service.get_gross_price(29.99, 0.08)
  assert_that(result).is_equal_to(32.39)
  assert_that(result).is_not_equal_to(32.40)

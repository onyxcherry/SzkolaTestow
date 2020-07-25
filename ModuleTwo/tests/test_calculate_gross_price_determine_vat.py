from assertpy import assert_that


def test_calculating_gross_price_for_determined_vat(vat_service, mocker):
  mocker.patch('app.vat_provider.VatProvider.get_vat_for_given_type',
               return_value=0.05)
  result = vat_service.get_gross_price(13.70, 'boots')
  assert_that(result).is_equal_to(14.38)
  assert_that(result).is_not_equal_to(14.39)

from app.vat_service import VatService

vat_service = VatService()


def test_calculate_gross_price_for_given_valid_vat():
  assert vat_service.get_gross_price(29.99, 0.08) == 32.39

import pytest


def test_throw_exception_when_invalid_vat_value(vat_service):
  with pytest.raises(ValueError) as value_error:
    vat_service.get_gross_price(18.59, 2.56)
    assert 'range' in str(value_error.value)
    assert '0' in str(value_error.value)
    assert '1' in str(value_error.value)

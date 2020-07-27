import json
from unittest import mock
from uuid import uuid1

from assertpy import assert_that

from app import Product

mocked_default_vat = 'app.vat_provider.VatProvider.get_default_vat'
mocked_determined_vat = 'app.vat_provider.VatProvider.get_vat_for_given_type'


@mock.patch(mocked_default_vat, return_value=0.23, autospec=True)
def test_jsoned_response_based_on_product(mocked_vat, vat_service):
  product = Product(int(uuid1()), 6.74, 'sweatshirt')
  result = vat_service.get_json(product, None, None)
  jsoned_result = json.loads(result)
  assert_that(jsoned_result).has_gross_price(8.29)
  assert_that(jsoned_result).has_net_price(6.74)
  assert_that(jsoned_result).has_product_type('sweatshirt')


@mock.patch(mocked_determined_vat, return_value=0.08, autospec=True)
def test_jsoned_response_based_on_given_price_and_type(mocked_vat, vat_service):
  net_price = 5.99
  product_type = 'books'
  result = vat_service.get_json(None, net_price, product_type)
  jsoned_result = json.loads(result)
  assert_that(jsoned_result).has_gross_price(6.47)
  assert_that(jsoned_result).has_net_price(5.99)
  assert_that(jsoned_result).has_product_type(product_type)

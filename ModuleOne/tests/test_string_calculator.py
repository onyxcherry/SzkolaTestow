import pytest

from app.calculator import StringCalculator

calculator = StringCalculator()


def test_blank_characters():
  assert calculator.add('') == 0, 'It should return 0'
  assert calculator.add('   ') == 0, 'It should return 0'


def test_one_number_given():
  assert calculator.add('-4') == -4, 'It should return given number'
  assert calculator.add('0') == 0, 'It should return given number'
  assert calculator.add('  123895 ') == 123895, 'It should return given number'


@pytest.mark.parametrize(
  'user_input, expected',
  [
    ('3,8', 3 + 8),
    ('5 ,  -7, 67', 5 + (-7) + 67),
    ('234, 32345,  123', 234 + 32345 + 123),
  ],
)
def test_adding_multiple_numbers(user_input, expected):
  assert (
      calculator.add(user_input) == expected
  ), 'It should return a sum of given numbers'

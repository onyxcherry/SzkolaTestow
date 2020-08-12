import math

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


def test_adding_floating_point_numbers():
  assert calculator.add(
    '7.3, 4') == 7.3 + 4, 'It should return a sum of given numbers. ' \
                          'Note the unexpected fraction at the end ' \
                          '(e.g. add .1 + 2. in the IDLE)'
  assert math.isclose(calculator.add('7.3, 4'), 11.3), \
    'It should return a sum of given numbers. Note the unexpected fraction ' \
    'at the end (e.g. add .1 + 2. in the IDLE)'


@pytest.mark.parametrize(
  'user_input, expected',
  [
    ('3,8', 3 + 8),
    ('5 ,  -7, 67', 5 + -7 + 67),
    ('234, 323.45,  123', 234 + 323.45 + 123),
    ('43, 567, .2, 789, 0, 12, 1234', 43 + 567 + .2 + 789 + 0 + 12 + 1234),
  ],
)
def test_adding_multiple_numbers(user_input, expected):
  assert (
      calculator.add(user_input) == expected
  ), 'It should return a sum of given numbers'

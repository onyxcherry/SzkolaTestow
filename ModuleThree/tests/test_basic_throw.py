from assertpy import assert_that


def test_basic_throw(bowling):
  for x in range(20):
    bowling.roll(0)
  assert_that(bowling.get_score()).is_equal_to(0)

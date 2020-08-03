from assertpy import assert_that


def test_strike(bowling):
  bowling.roll(10)
  bowling.roll(7)
  bowling.roll(4)
  for x in range(16):
    bowling.roll(0)
  assert_that(bowling.get_score()).is_equal_to(32)

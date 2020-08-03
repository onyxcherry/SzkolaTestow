from assertpy import assert_that


def test_spare(bowling):
  bowling.roll(4)
  bowling.roll(6)
  bowling.roll(7)
  for x in range(17):
    bowling.roll(0)
  assert_that(bowling.get_score()).is_equal_to(24)

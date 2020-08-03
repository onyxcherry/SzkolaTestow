from assertpy import assert_that


def test_9_and_miss(bowling):
  for _ in range(10):
    bowling.roll(9)
    bowling.roll(0)
  assert_that(bowling.get_score()).is_equal_to(90)
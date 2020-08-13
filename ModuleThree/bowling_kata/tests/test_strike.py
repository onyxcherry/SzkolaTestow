from assertpy import assert_that


def test_strike_at_the_beginning(bowling):
  bowling.roll(10)
  bowling.roll(7)
  bowling.roll(4)
  for x in range(16):
    bowling.roll(0)
  assert_that(bowling.get_score()).is_equal_to(32)


def test_strike_at_the_last_frame(bowling):
  for x in range(18):
    bowling.roll(0)
  bowling.roll(10)
  bowling.roll(6)
  bowling.roll(7)
  assert_that(bowling.get_score()).is_equal_to(23)

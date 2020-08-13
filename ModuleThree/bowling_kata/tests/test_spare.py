from assertpy import assert_that


def test_spare_at_the_beginning(bowling):
  bowling.roll(4)
  bowling.roll(6)
  bowling.roll(7)
  for x in range(17):
    bowling.roll(0)
  assert_that(bowling.get_score()).is_equal_to(24)


def test_spare_at_the_last_frame(bowling):
  for x in range(18):
    bowling.roll(0)
  bowling.roll(3)
  bowling.roll(7)
  bowling.roll(6)
  assert_that(bowling.get_score()).is_equal_to(16)

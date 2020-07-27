from assertpy import assert_that


def test_missed_throws(bowling):
  for x in range(20):
    bowling.roll(0)
  assert_that(bowling.get_score()).is_equal_to(0)


def test_basic_throws(bowling):
  for x in range(20):
    bowling.roll(3)
  assert_that(bowling.get_score()).is_equal_to(60)


def test_throw_frame(bowling):
  bowling.roll(5)
  bowling.roll(4)
  assert_that(bowling.get_score()).is_equal_to(5 + 4)

from assertpy import assert_that


def test_master_throws(bowling):
  for x in range(12):
    bowling.roll(10)
  assert_that(bowling.get_score()).is_equal_to(300)

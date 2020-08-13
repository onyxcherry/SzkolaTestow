from assertpy import assert_that


def test_9_and_miss(bowling):
  for _ in range(10):
    bowling.roll(9)
    bowling.roll(0)
  assert_that(bowling.get_score()).is_equal_to(90)


def test_10_pairs_of_10_and_spare_with_final_5(bowling):
  for _ in range(21):
    bowling.roll(5)
  assert_that(bowling.get_score()).is_equal_to(150)


def test_master_throws(bowling):
  for x in range(12):
    bowling.roll(10)
  assert_that(bowling.get_score()).is_equal_to(300)
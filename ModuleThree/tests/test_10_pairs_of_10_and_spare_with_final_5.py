from assertpy import assert_that


def test_10_pairs_of_10_and_spare_with_final_5(bowling):
  for _ in range(21):
    bowling.roll(5)
  assert_that(bowling.get_score()).is_equal_to(150)
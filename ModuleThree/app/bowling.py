class Bowling:
  def __init__(self) -> None:
    self.rolls = [0] * 22
    self.the_roll = 0

  def roll(self, pins: int) -> None:
    self.rolls[self.the_roll] = pins
    self.the_roll += 1

  def get_score(self) -> int:
    cursor = 0
    score = 0
    for x in range(10):
      if self.rolls[cursor] == 10:
        score += 10 + self.rolls[cursor + 1] + self.rolls[cursor + 2]
        cursor += 1
      elif self.check_if_spare(cursor):
        score += 10 + self.rolls[cursor + 2]
        cursor += 2
      else:
        score += self.rolls[cursor] + self.rolls[cursor + 1]
        cursor += 2
    return score

  def check_if_spare(self, cursor: int) -> bool:
    return self.rolls[cursor] + self.rolls[cursor + 1] == 10

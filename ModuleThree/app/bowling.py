class Bowling:
  def __init__(self):
    self.score = 0
    self.pins = []
    self.cursor = 0

  def roll(self, knocked_pins):
    self.pins.append(knocked_pins)
    # self.counter += 1

  def get_score(self):
    self.score = sum(self.pins)
    for x in range(10):
      if self.check_if_spare():
        self.score += self.pins[self.cursor + 2]
        self.cursor += 2
      elif self.check_if_strike():
        self.score += self.pins[self.cursor + 1]
        self.score += self.pins[self.cursor + 2]
        self.cursor += 1
      else:
        self.cursor += 2
    return self.score

  def check_if_range(self):
    if self.cursor > len(self.pins) or self.cursor + 1 > len(self.pins):
      return True
    return False

  def check_if_spare(self):
    if self.check_if_range():
      return False
    return self.pins[self.cursor] + self.pins[self.cursor + 1] == 10

  def check_if_strike(self):
    if self.check_if_range():
      return False
    return self.pins[self.cursor] == 10

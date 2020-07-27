class Bowling:
  def __init__(self):
    self.score = 0
    self.pins = []
    self.counter = 0

  def roll(self, knocked_pins):
    self.pins.append(knocked_pins)
    # self.counter += 1

  def get_score(self):
    self.score = sum(self.pins)
    for x in range(20):
      if self.check_if_spare():
        self.score += self.pins[self.counter + 2]
        self.counter += 1
    return self.score

  def check_if_spare(self):
      return self.pins[self.counter] + self.pins[self.counter + 1] == 10


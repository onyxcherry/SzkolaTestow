class Bowling:
  def __init__(self):
    self.score = 0

  def roll(self, knocked_pins):
    self.score += knocked_pins

  def get_score(self):
    return self.score

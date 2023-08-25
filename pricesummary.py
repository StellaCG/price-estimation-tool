class PriceSummary:

  def __init__(self, avg, min, max):
    self.avg = avg
    self.min = min
    self.max = max

  def __str__(self):
    return f"\naverage price: {self.avg}\nlowest price: {self.min}\nhighest price: {self.max}"
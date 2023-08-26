class PriceSummary:

  def __init__(self, avg, min, max):
    self.avg = avg
    self.min = min
    self.max = max

  def __str__(self):
    return f"\naverage price: {self.avg}\nlowest price: {self.min}\nhighest price: {self.max}"

class Listing:
  def __init__(self, price, info):
    self.info = info
    self.price = price

  def __str__(self):
    return f"${self.price}\t({self.info})"

class EbayListing(Listing):
  def __init__(self, info, price, days):
    super().__init__(price, info)
    self.info = info
    self.price = price
    self.date = days

  def __str__(self):
    return f"{self.info}\n\t({self.price} sold {self.date} ago)"

def print_results(results, r):
  for i in range(r):
    print(results[0][i])
  print(results[1])
  print(f"results shown: {r}")
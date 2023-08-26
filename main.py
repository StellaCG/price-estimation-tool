from ebay import *
from monsterax import *
from plantly import *
from helpers import *
# from matplotlib import pyplot as plt

# todo: weigh plantly as 30% of average if only returns
# one listing

# removed graphing for now

def main():
  query = 'thai constellation' # input("Enter a search term: ")
  numresults = 20 # int(input("\nHow many results: "))
  strict_search = True
  r1 = numresults
  r2 = numresults
  r3 = numresults
  
  ebay_results = ebay_search(query, numresults)
  monsterax_results = monsterax_search(query, numresults, strict_search)
  plantly_results = plantly_search(query, numresults)
  
  if numresults > len(ebay_results[0]):
    r1 = len(ebay_results[0])
  if numresults > len(monsterax_results[0]):
    r2 = len(monsterax_results[0])
  if numresults > len(plantly_results[0]):
    r3 = len(plantly_results[0])

  print("eBay results:\n")
  print_results(ebay_results, r1)

  print("\nMonsteraX results:\n")
  print_results(monsterax_results, r2)

  print("\nPlantly results:\n")
  print_results(plantly_results, r3)

  # calc total average across sites by
  # weighing avgs by number of items
  tnr = r1 + r2 + r3
  if tnr != 0:
    overall_average = (ebay_results[1].avg * (r1 / tnr)) + (monsterax_results[1].avg * (r2 / tnr) + (plantly_results[1].avg * (r3 / tnr)))
    print(f"\noverall average price: {round(overall_average, 2)} across {tnr} items")

if __name__ == "__main__":
  main()



'''plt.scatter([i for i in range(1, numresults+1)], [float(l.price[1:]) for l in results[0][:numresults]])
  price_over_time = []
  for i in range(numresults+1):
    price_over_time.append([results[0][i].date.days, float(results[0][i].price[1:])])

  plt.plot([p[0] for p in price_over_time], [p[1] for p in price_over_time])
  # plt.plot([d.date.days for d in results[0][:numresults]], [float(l.price[1:]) for l in results[0][:numresults]])
  plt.show()'''
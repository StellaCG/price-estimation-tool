from ebay import *
from monsterax import *
# from matplotlib import pyplot as plt

# todo: walmart, amazon
# fix bug in line 20 with price ranges

# removed graphing for now

def main():
  query = 'florida beauty' # input("Enter a search term: ")
  numresults = 5 # int(input("\nHow many results: "))
  r1 = numresults
  r2 = numresults
  
  ebay_results = ebay_search(query, numresults)
  monsterax_results = monsterax_search(query, numresults, True)
  
  if numresults > len(ebay_results[0]):
    r1 = len(ebay_results[0])
  elif numresults > len(monsterax_results[0]):
    r2 = len(monsterax_results[0])

  print("eBay results:\n")
  for i in range(r1):
    print(ebay_results[0][i])
  print(ebay_results[1])
  print(f"results shown: {r1}")

  print("\nMonsteraX results:\n")
  for i in range(r2):
    print(monsterax_results[0][i])
  print(monsterax_results[1])
  print(f"results shown: {r2}")

if __name__ == "__main__":
  main()



'''plt.scatter([i for i in range(1, numresults+1)], [float(l.price[1:]) for l in results[0][:numresults]])
  price_over_time = []
  for i in range(numresults+1):
    price_over_time.append([results[0][i].date.days, float(results[0][i].price[1:])])

  plt.plot([p[0] for p in price_over_time], [p[1] for p in price_over_time])
  # plt.plot([d.date.days for d in results[0][:numresults]], [float(l.price[1:]) for l in results[0][:numresults]])
  plt.show()'''
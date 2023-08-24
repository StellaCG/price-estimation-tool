from ebay import *
# from matplotlib import pyplot as plt

# todo: walmart, amazon
# fix bug in line 20 with price ranges

# removed graphing for now

def main():
  query = input("Enter a search term: ")
  numresults = int(input("\nHow many results: "))
  results = ebay_search(query, numresults)

  if numresults > len(results[0]):
    numresults = len(results[0])
  for i in range(numresults):
    print(results[0][i])
  print(results[1])

  print(f"\nresults shown: {numresults}")

if __name__ == "__main__":
  main()



'''plt.scatter([i for i in range(1, numresults+1)], [float(l.price[1:]) for l in results[0][:numresults]])
  price_over_time = []
  for i in range(numresults+1):
    price_over_time.append([results[0][i].date.days, float(results[0][i].price[1:])])

  plt.plot([p[0] for p in price_over_time], [p[1] for p in price_over_time])
  # plt.plot([d.date.days for d in results[0][:numresults]], [float(l.price[1:]) for l in results[0][:numresults]])
  plt.show()'''
from bs4 import BeautifulSoup as bs
import requests
import locale
import re

from helpers import *

locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')

def monsterax_search(query, MAX_RESULTS, STRICT_SEARCH):
  search_url = 'https://www.monsterax.com/marketplace?keywords=' + query # '&sort=-pub_closedAuctionInt%2Cpub_hasStockInt%2C-pub_currentAmount'
  response = requests.get(search_url)
  soup = bs(response.text, 'html.parser')
  listings = []
  
  start = soup.text.find('Sort by:Sale')
  test_str = soup.text[start+8:]
  test_sub = '$'
  test_sub_end = '🌱'
  res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)]
  res_end = [i for i in range(len(test_str)) if test_str.startswith(test_sub_end, i)]

  if MAX_RESULTS > len(res_end):
    MAX_RESULTS = len(res_end)

  average_price = 0.00
  lowest_price = 99999.00
  highest_price = 0.00
  parsed_price = 0.00
  
  for i in range(len(res_end)):
    num = re.search(r'[a-z]', test_str[res[i]:res_end[i]], re.I)
    curr = test_str[res[i]+len(num[0]):res_end[i]-1]
    
    if(STRICT_SEARCH):
      if query in curr:
        listings.append(Listing(curr[:num.start()-1], curr[num.start()-1:]))
        
        parsed_price = locale.atof(curr[:num.start()-1])
        average_price += parsed_price
        if parsed_price > highest_price:
          highest_price = parsed_price
        if parsed_price < lowest_price:
          lowest_price = parsed_price
        if len(listings) > MAX_RESULTS:
          break
    else:
      listings.append(Listing(curr[:num.start()-1], curr[num.start()-1:]))
      
      parsed_price = locale.atof(curr[:num.start()-1]) 
      average_price += parsed_price
      if parsed_price > highest_price:
        highest_price = parsed_price
      if parsed_price < lowest_price:
        lowest_price = parsed_price
    

  # double check num of results
  if MAX_RESULTS > len(listings):
    MAX_RESULTS = len(listings)
  if MAX_RESULTS != 0:
    average_price /= MAX_RESULTS
  
  pricesum = PriceSummary(round(average_price, 2), lowest_price, highest_price)
  return(listings, pricesum)
                

            
  
  
  
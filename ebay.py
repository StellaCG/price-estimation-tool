from bs4 import BeautifulSoup as bs
import requests
import locale
from datetime import datetime

from helpers import *

locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')

def ebay_search(query, MAX_RESULTS):
  search_url = "https://www.ebay.com/sch/i.html?_nkw=" + query + "&_Sold=1&LH_Sold=1&LH_Complete=1"

  response = requests.get(search_url)
  soup = bs(response.text, 'html.parser')

  listings = []
  names = soup.select('.s-item__title span[role="heading"]')
  prices = soup.select('.s-item__detail--primary span[class="s-item__price"]')
  days_dt = soup.select('.s-item__title--tag span[class="POSITIVE"]')

  for i in range(1, len(names)):
    listings.append(
      EbayListing(
        names[i].text, prices[i].text,
        datetime.today() -
        datetime.strptime(days_dt[i - 1].text[6:], '%b %d, %Y')))

  average_price = 0.00
  lowest_price = 99999.00
  highest_price = 0.00
  parsed_price = 0.00

  # cap max results
  if MAX_RESULTS > len(listings):
    MAX_RESULTS = len(listings)
  
  for i in range(1, MAX_RESULTS):
    # check for price ranges and default to lowest
    if "to" in prices[i].text:
      parsed_price = locale.atof(prices[i].text.split()[0][1:])
    else:
      parsed_price = locale.atof(prices[i].text[1:])
    average_price += parsed_price
    if parsed_price > highest_price:
      highest_price = parsed_price
    if parsed_price < lowest_price:
      lowest_price = parsed_price

  if MAX_RESULTS != 0:
    average_price /= MAX_RESULTS
  pricesum = PriceSummary(round(average_price, 2), lowest_price, highest_price)
  return (listings, pricesum)

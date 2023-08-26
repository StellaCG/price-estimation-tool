from bs4 import BeautifulSoup as bs
import requests
import locale
from helpers import *

locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')

def plantly_search(query, MAX_RESULTS):
  # construct search url
  search_url = 'https://plantly.io/?post_type=product&s=' + query
  response = requests.get(search_url)
  soup = bs(response.text, 'html.parser')

  # scrape listings
  listings = []
  info = [i.text for i in soup.find_all("h2", class_="woo-loop-product__title")]
  prices = [p.find("span", class_="woocommerce-Price-amount amount").text[1:] for p in soup.find_all("div", class_="mf-product-details")]

  if MAX_RESULTS > len(info):
    MAX_RESULTS = len(info)
    
  average_price = 0.00
  lowest_price = 99999.00
  highest_price = 0.00
  parsed_price = 0.00

  # populate list of listings
  for i in range(MAX_RESULTS):
    listings.append(Listing(prices[i], info[i]))

    parsed_price = locale.atof(prices[i])
    average_price += parsed_price
    if parsed_price > highest_price:
      highest_price = parsed_price
    if parsed_price < lowest_price:
      lowest_price = parsed_price

  if MAX_RESULTS != 0:
    average_price /= MAX_RESULTS
  pricesum = PriceSummary(round(average_price, 2), lowest_price, highest_price)
  return(listings, pricesum)
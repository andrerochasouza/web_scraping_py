from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, urlretrieve, Request
from urllib.error import HTTPError, URLError
import pandas as pd

# # pegar as trends do twitter
# url = 'https://twitter.com/i/trends'
# twitter = req.get(url)
# twitter_soup = bs(twitter.text, 'html.parser')
# print(twitter_soup)

# main_page_twitter = twitter_soup.find('main', {'role': 'main'})
# print(main_page_twitter)

# trends = []

# print(trends)


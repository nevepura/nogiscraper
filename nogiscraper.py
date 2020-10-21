import requests
from bs4 import BeautifulSoup
import re

def get_from_sanjuro():
  page = requests.get("http://www.stage48.net/forum/index.php?threads/subbed-nogizaka-shows-thread.6775/page-309")

  soup = BeautifulSoup(page.content,'html.parser')

  posts = soup.find_all('li', attrs={'data-author':'Sanjuro'})


  for post in posts:
    if(re.search("Nogizaka Under Construction ep279", post.text)):
      print('Found!')
      
      message = post.find('blockquote')
      links = message.find_all('a')
      
      link_softsub = links[1].text
      link_hardsub = links[2].text
      return [link_softsub, link_hardsub]

    else:
      print('Not found')
      return []

print(get_from_sanjuro())



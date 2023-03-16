from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from fake_useragent import UserAgent
import requests

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}
htmlContent = requests.get('https://www.booking.com/searchresults.tr.html?ss=Belgrad&ssne=Belgrad&ssne_untouched=Belgrad&label=gen173rf-1BCAEoggI46AdIM1gDaOQBiAEBmAEouAEXyAEM2AEB6AEBiAIBogINcHJvamVjdHByby5pb6gCA7gClNjBoAbAAgHSAiQ2OTVmZWQ2My1jMDcxLTQwOTEtYjZjMC0zZjZhMjIwNDM5YjDYAgXgAgE&sid=00908ca4bb723e389dea8cabf3a08eaf&aid=304142&lang=tr&sb=1&src_elem=sb&src=searchresults&dest_id=-74897&dest_type=city&checkin=2023-04-12&checkout=2023-04-13&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure', headers=header)

soup= BeautifulSoup(htmlContent.content, 'html.parser')

title_list = []
location_list = []
ratings_list = []
review_counts = []


for item in soup.find_all('div', {'data-testid': 'property-card'}):
    try:  
        title = item.find('div', class_='fcab3ed991').get_text(strip=True)
        title_list.append(title)
    except AttributeError:
        title_list.append('not available')
    try:  
        location = item.find('span', {'data-testid': 'address'}).get_text(strip=True)
        location_list.append(location)
    except AttributeError:
        location_list.append('not available')
    try:
        rating = item.find('div', class_='d10a6220b4').get_text(strip=True)
        ratings_list.append(rating)
    except AttributeError:
        ratings_list.append('not available')

    try:    
        review = item.find('div', class_='db63693c62').get_text(strip=True)
        review_counts.append(review)
    except AttributeError:
        review_counts.append('not available')

print((title_list))
print((location_list))
print((ratings_list))
print(review_counts)

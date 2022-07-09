import requests
import re

url = "https://www.rokomari.com"

res = requests.get(url)
text = res.text
organized_text = re.sub("\s+", " ", text)

item_half_links = re.findall('<div class="book-list-wrapper ">\s*<a href="(.+?)"', organized_text)
item_full_links = ["https://www.rokomari.com" + x for x in item_half_links]


print("Rokomari's All Links")
for item in item_full_links:
    print("Elements Link:", item)

item_info = re.findall(r'{.*?"url":"(.+?)"', text)
full_link = ["https://www.rokomari.com" + x for x in item_info]
for dsd in full_link:
    print("Elements Link:", dsd)

